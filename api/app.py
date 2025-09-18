from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

model = joblib.load('Model/dt_selected_features.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        required_fields = [
                "phq_score",
                "depressiveness",
                "depression_treatment",
                "anxiety_diagnosis",
                "anxiety_treatment"
        ]

        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({"error": f"Campos ausentes: {', '.join(missing_fields)}"}), 400

        features = [
            float(data["phq_score"]),
            int(data["depressiveness"]),
            int(data["depression_treatment"]),
            int(data["anxiety_diagnosis"]),
            int(data["anxiety_treatment"]),
        ]

        input_data = pd.DataFrame([features], columns=[
            'phq_score',
            'depressiveness',
            'depression_treatment',
            'anxiety_diagnosis',
            'anxiety_treatment'
        ])

        prediction = model.predict(input_data)[0]
        confidence_score = max(model.predict_proba(input_data)[0])

        return jsonify({
            "confidence_score": round(confidence_score, 4),
            "prediction_result": int(prediction)
        }), 200

    except ValueError:
        return jsonify({"error": "Erro ao converter os dados. Por favor verifique os valores informados."}), 400
    except KeyError:
        return jsonify({"error": "Dados de entrada incorretos ou ausentes."}), 400
    except Exception as e:
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
