# Análise de dados de doenças cardiovasculares
Por [José Vitor](https://github.com/jsvitor), [Claudiano Lima](https://github.com/claudianopl), [Eugenio Dorneles](https://github.com/eugeniol2) e [Júlia Aguiar](https://github.com/juliaguiar1).

> ### Sinopse do Conteúdo
> * Mineração de Dados;
> * Aprendizado de Máquina;
> * Ciência de Dados;
> * Ferramentas de Mineração e Análise de Dados;
> * Análises Estatísticas;
> * Desenvolvimento de Aplicações em Problemas Reais que Demandam Análises no Cenário de Big Data.

<details>
	<summary>Ementa</summary>

### OBJETIVOS DA DISCIPLINA

> Permitir que os estudantes aprendam a aplicar ferramentas e métodos de ciência de dados em
problemas reais, integrando suas soluções em projetos de sistemas de informação.
      
* Introduzir conceitos de mineração de dados, aprendizado de máquina e estatística;
* Apresentar técnicas básicas relacionadas a estatística e aprendizado de máquina;
* Investigar problemas e conjuntos de dados que podem contribuir para um trabalho unificado para as demais disciplinas cursadas pelos estudantes;
* Introduzir conceitos gerais relacionados ao desenvolvimento de software em equipes, como a análise estática de código e o uso de ferramentas de versionamento.

### CONTEÚDO PROGRAMÁTICO
1. Identificação de problemas que podem ser investigados com ciência de dados;
2. Investigação de técnicas de estatística e de aprendizado de máquina que mais se adéquam à solução proposta;
3. Apresentação dos resultados;
4. Ferramentas e métodos para desenvolvimento de software em time;

### BIBLIOGRAFIA
> #### BÁSICA:
> 1. Documentação do Pandas. Disponível em https://pandas.pydata.org/
> 2. Documentação do Scikit-Learn. Disponível em https://scikit-learn.org/
> 3. Documentação do Streamlit. Disponível em https://streamlit.io/
>
> #### COMPLEMENTAR:
>
> 1. Grus, Joel. Data science from scratch: first principles with python. O&#39;Reilly Media, 2019.
> 2. Géron, Aurélien. Hands-on machine learning with Scikit-Learn, Keras, and
> TensorFlow: Concepts, tools, and techniques to build intelligent systems. O&#39;Reilly
> Media, 2019.
> 3. WITTEN, I. H; FRANK, Eibe; HALL, Mark A. Data mining: practical machine
> learning tools and techniques. 3rd ed. Burlington, MA: Elsevier Morgan Kaufmann,
> 2011. xxxi, 629 p. (The Morgan Kaufmann series in data management systems) ISBN
> 9780123748560.
> 4. ELMASRI, Ramez; NAVATHE, Shamkant B. Sistemas de banco de dados. 6.ed. São
> Paulo: Pearson Addison Wesley, 2011. 788 p. ISBN 9788579360855.
> 5. RUSSELL, S.; NORVIG, P. Inteligência artificial. 2 ed. Elsevier, 2004.

> RECIFE, 15 de fevereiro de 2022
>
> [Gabriel Alves de Albuquerque Júnior](gaaj-ufrpe)
> Docente Responsável

</details>  

> Este repositório dedicasse a versionar o conteúdo das atividades práticas da disciplina de PISI III, ofertada pelo curso de Bacharelado em Sistemas de Informação da UFRPE.
> Caso você queira saber mais detalhes sobre esta disciplina, acesse a [página](https://jsvitor.github.io/heart-disease-data-analysis/) ou vá ao branch [gh-pages](https://github.com/jsvitor/heart-disease-data-analysis/tree/gh-pages).

> 👉🏼 Neste branch e, em outros do repositório (com exceção do `gh-pages`), você encontrará o versionamento do projeto `Heart disease data analysis`.
> Que servirá como a inteligência do aplicativo [Unleash Health](https://github.com/jsvitor/unleash_health_flutter), desenvolvido com Flutter, como requisito avaliativo da disciplina de Desenvolvimento de Sistemas de Informação.

### Estrutura de diretórios e arquivos
````
      .
      ├── data
      │   ├── personal-key-indicators-of-heart-disease-dataset.csv
      │   └── personal-key-indicators-of-heart-disease-data-dictionary.md
      ├── pipeline                 # These could be docker containers related code, scripts, workflow related code, etc.
      │   ├── dags
      │   │    ├── ingestion_dag.py
      │   │    ├── validation_dag.py
      │   │    ├── regretion_dag.py
      │   │    ├── forecasting_dag.py
      │   │    └── clustering_dag.py
      |   └── ...
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
      
````
