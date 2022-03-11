# Análises e jobs de machine learning sobre doenças cardíacas

Este repositório tem ...


### Estrutura de diretórios e arquivos
      .
      ├── data
      │   ├── personal-key-indicators-of-heart-disease-dataset.csv
      │   └── personal-key-indicators-of-heart-disease-data-dictionary.md
      ├── pipeline                 # These could be docker containers related code, scripts, workflow related code, etc.
      │   ├── airflow
      │   │    ├── dags
      │   │    |   ├── regretion_dag.py
      │   │    │   ├── forecasting_dag.py
      │   │    │   ├── validation_dag.py
      │   │    │   └── clustering_dag.py
      |   │    └── ...
      │   ├── config
      │   └── setup.sh
      │
      ├── models             # The folder that consists of files representing trained/retrained models as part of build jobs, etc
      │   ├── project_build_id             # the result of the model
      │   ├── projectname_date_time             
      │   └── ...
      │
      ├── src             # The folder that consists of the source code related to data gathering, data preparation, feature extraction, etc.
      │   ├── data_gathering.py
      │   ├── data_preparation.py             
      │   └── feature_extraction.py
      ├── Dockerfile
      ├── docker-compose.yml
      ├── .gitignore
      ├── requirements.txt
      ├── .editorconfig
      └── README.md
      
