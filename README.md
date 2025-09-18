
# Análise da Saúde Mental de jovens universitários por meio de técnicas de Machine Learning

Trabalho de Conclusão de Curso II – Bacharelado em Sistemas de Informação (UFERSA)

Este repositório apresenta o uso de técnicas de Machine Learning para analisar dados de saúde mental de 787 estudantes da Universidade de Lahore. O projeto utiliza algoritmos clássicos e avançados para identificar padrões e gerar insights a partir do dataset `depression_anxiety_data.csv`.




![App Screenshot](https://www.planetreebrasil.com.br/wp-content/uploads/2023/08/Problemas-de-saude-mental-podem-variar-desde-preocupacoes-diarias-normais-ate-condicoes-mais-graves.-Imagem-Shutterstock.jpg)


## 💻Stack utilizada

**Linguagem:** Python

**Bibliotecas:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Graphviz, Imbalanced-Learn, Collections 

**Ambiente de Desenvolvimento:**  Jupyter Lab, Anaconda Navigator
## 📊 Metodologia utilizada

Pré-processamento dos Dados:
- Tratamento de valores ausentes.
- Normalização e codificação de variáveis categóricas.

Modelos de Machine Learning:
- Naive Bayes (NB)
- Random Forest (RF)
- Decision Tree (DT)
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

Métricas de Avaliação:
 - Accuracy
 - Precision
 - Recall
 - F1-Score 

Validação dos Modelos:
- Divisão Holdout (Treinamento/Teste).
- Validação Cruzada.

# API de predição de Saúde Mental 🧠

A API foi desenvolvida em **Flask** e utiliza o modelo Decision Tree previamente treinado para prever diagnósticos relacionados à depressão com base nas melhores características do dataset.

## 📂 Estrutura do Projeto

```
├─ Dataset/
│  └─ depression_anxiety_data.csv
├─ Modelos/
│  ├─ decision_tree.ipynb
│  ├─ knn.ipynb
│  ├─ naive_bayes.ipynb
│  ├─ random_forest.ipynb
│  └─ svm.ipynb
├─ api/
│  ├─ Model/
│  │  └─ dt_selected_features.joblib
│  ├─ requirements.txt
└─ └─ app.py
```

## 🚀 Como Executar a API

### 1. Clonar o Repositório
```bash
git clone https://github.com/WesleydosSantos/machine-learning-tecnicas.git
```

### 3. Abra o repositório clonado
```bash
cd machine-learning-tecnicas
```

### 4. Instale as dependências necessárias
```bash
pip install -r requirements.txt
```

### 5. Execute a api
```bash
python app.py
```

#### 5.1 Faça uma requisição

| Tipo de Requisição  | URL | Descrição |
| ------------- | ------------- | ------------- |
| POST | http://localhost:5000/predict | Retorna a predição juntamente com a confiança do modelo|

Exemplo de JSON
```bash
{
    "phq_score": 18,
    "depressiveness": 1,
    "depression_treatment": 1,
    "anxiety_diagnosis": 1,
    "anxiety_treatment": 1
}
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) 
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626.svg?style=flat&logo=Jupyter)](https://jupyterlab.readthedocs.io/en/stable)

