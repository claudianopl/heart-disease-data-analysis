import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')

types = ["Média","Absoluto","Mediana","Máximo","Mínimo"]

label_attr_dict = {
  'Heart Disease': 'HeartDisease',
  'BMI': 'BMI',
  'Smoking': 'Smoking',
  'Alcohol Drinking': 'AlcoholDrinking',
  'Stroke': 'Stroke',
  'Physical Health': 'PhysicalHealth',
  'Mental Health': 'MentalHealth',
  'Diff Walking': 'DiffWalking',
  'Sex': 'Sex',
  'Age Category': 'AgeCategory',
  'Race': 'Race',
  'Diabetic': 'Diabetic',
  'Physical Activity': 'PhysicalActivity',
  'Gen Health': 'GenHealth',
  'Sleep Time': 'SleepTime',
  'Asthma': 'Asthma',
  'Kidney Disease': 'KidneyDisease',
  'Skin Cancer': 'SkinCancer'
}
label_attr_dict_heart_disease = {
  'BMI': 'BMI',
  'Physical Health': 'PhysicalHealth',
  'Mental Health': 'MentalHealth',
  'Sleep Time': 'SleepTime',
}
types_dict = {
  'Média': 'Mean',
  'Absoluto': 'Absolute',
  'Mediana': 'Median',
  'Máximo': 'Maximum',
  'Mínimo': 'Minimum',
}

def group_measure_by_attribute(aspect,attribute,measure):
    df_data = ds
    measure = types_dict[measure]
    if(measure == "Absolute"):
      df_return = df_data.groupby([aspect]).sum()            
    
    if(measure == "Mean"):
        df_return = df_data.groupby([aspect]).mean()
        
    if(measure == "Median"):
        df_return = df_data.groupby([aspect]).median()
    
    if(measure == "Minimum"):
        df_return = df_data.groupby([aspect]).min()
    
    if(measure == "Maximum"):
        df_return = df_data.groupby([aspect]).max()

    df_return["aspect"] = df_return.index
    
    return df_return

def plot_x_per_team(attr, measure):
  rc = {'figure.figsize':(8,4.5),
          'axes.facecolor':'#0e1117',
          'axes.edgecolor': '#0e1117',
          'axes.labelcolor': 'white',
          'figure.facecolor': '#0e1117',
          'patch.edgecolor': '#0e1117',
          'text.color': 'white',
          'xtick.color': 'white',
          'ytick.color': 'white',
          'grid.color': 'grey',
          'font.size' : 8,
          'axes.labelsize': 12,
          'xtick.labelsize': 8,
          'ytick.labelsize': 12}
  plt.rcParams.update(rc)
  fig, ax = plt.subplots()
  attribute = label_attr_dict_heart_disease[attr]
  df_plot = pd.DataFrame()
  df_plot = group_measure_by_attribute("HeartDisease", attribute, measure)
  ax = sns.barplot(x="aspect", y=attribute, data=df_plot.reset_index(), color = "#b80606")
  y_str = measure + " " + attr + " por doenças cardiovasculares"
  if measure == "Absolute":
        y_str = measure + " " + attr
  if measure == "Minimum" or measure == "Maximum":
      y_str = measure + " " + attr + "in a Game"
  ax.set(xlabel = "Heart Disease", ylabel = y_str)
  plt.xticks(rotation=66,horizontalalignment="right")

  st.pyplot(fig)

def get_unique_ages_modified(df_data):
  unique_ages = np.unique(df_data.AgeCategory).tolist()
  ages_modified = []
  for s,age in enumerate(unique_ages):
    if s==0:
        age = "‏‏‎ ‎‏‏‎ ‎" + age
    if s==len(unique_ages)-1:
        age = age + "‏‏‎ ‎‏‏‎ ‎"
    ages_modified.append(age.replace("-","/"))

  return(ages_modified)

def filter_ages(df_data, start_ages, end_ages):
  df_filtered_ages = pd.DataFrame()
  ages = np.unique(df_data.AgeCategory).tolist() 
  start_raw = start_ages.replace("/","-").replace("‏‏‎ ‎‏‏‎ ‎","") 
  end_raw = end_ages.replace("/","-").replace("‏‏‎ ‎‏‏‎ ‎","") 
  start_index = ages.index(start_raw)
  end_index = ages.index(end_raw)+1
  ages_selected = ages[start_index:end_index]
  df_filtered_ages = df_data[df_data['AgeCategory'].isin(ages_selected)]
  return df_filtered_ages

def data_exploration():
  st.sidebar.markdown("**Selecione o intervalo de dados que você deseja analisar:** 👇")
  unique_ages = get_unique_ages_modified(ds)
  start_ages, end_ages = st.sidebar.select_slider('Selecione a faixa etária que deseja incluir', unique_ages, value = ["‏‏‎ ‎‏‏‎ ‎18/24","80 or older‏‏‎ ‎‏‏‎ ‎"])
  df_data_filtered_ages = filter_ages(ds, start_ages, end_ages)

  dsOnlyHeartDiseaseYes = df_data_filtered_ages[df_data_filtered_ages['HeartDisease'] == 'Yes']

  ageOrder = ["80 or older", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "45-49","40-44", "35-39", "30-34", "25-29", "18-24"]

  histogramSexCount = px.histogram(df_data_filtered_ages, x="Sex", color="Sex",  color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})

  histogramAgeCategory = px.histogram(dsOnlyHeartDiseaseYes, x="AgeCategory", color="Sex", barmode="group", color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})
  df = px.data.tips()

  heatMap = px.density_heatmap(df_data_filtered_ages, x="AgeCategory", y="Sex", category_orders={"AgeCategory": ageOrder})

  y = df_data_filtered_ages['AgeCategory'].value_counts()
  # pieChart = px.pie(y, values=y, names=y.index )
  # pieChart.update_traces(textposition='inside', textinfo='percent+label')

  ageOrder = ["80 or older", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "45-49","40-44", "35-39", "30-34", "25-29", "18-24"]
  pieChart = px.histogram(df_data_filtered_ages, x="AgeCategory", category_orders={"AgeCategory": ageOrder})

  st.title('Análise exploratória de dados')

  st.markdown('### Seção 01: Existe alguma relação entre os  problemas cardiovasculares apresentado nos pacientes e suas características fisiológicas?')

  row0_space1, row0_space2 = st.columns(2)

  with row0_space1:
    st.markdown("#### Como está a dispersão de dados relacionados à idade no dataset ?")
    st.plotly_chart(pieChart)
    st.markdown('Nota-se que a grande maioria das faixas etárias estão relativamente balanceadas, com uma maior predominância nas idades 70-74, 60-64 e 65-69.')

  with row0_space2:
    st.markdown("""#### A partir de outra perspectiva, como a idade e sexo estão dispersos no dataset?""")
    st.plotly_chart(heatMap)
    st.markdown('Percebe-se que, como antes visto, as idades 70-74, 65-69 e 60-64 estão mais presentes em ambos os gêneros, entretanto, existem mais registros do sexo feminino.')
  

  row1_space1, row2_space2 = st.columns(2)

  with row1_space1:
    st.markdown("""#### Os gêneros estão balanceados no dataset ?""")
    st.plotly_chart(histogramSexCount)
    st.markdown("Nota-se que existem mais mulheres no dataset.")

  with row2_space2:
    st.markdown("""#### Agora, apos filtrar o dataset para casos positivos, como esses casos se comportam em relação à idade e sexo do paciente? """)
    st.plotly_chart(histogramAgeCategory)
    st.markdown('De acordo com os gráfico é perceptível que os casos positivos começam a aumentar de forma mais notável a partir da faixa etária de 50-54 anos em ambos os sexos, é também visível que o sexo que mais possui casos é o masculino.')

  row2_space1, row2_space2 = st.columns((1.2, .8))

  with row2_space1:
    st.markdown("""### Pontos interessantess da seção 1:""")
    st.markdown(" - A idade mostrou ser um fator importante para o aumento dos casos positivos.")
    st.markdown(" - O sexo também tem um grau de relevância, tendendo aumentar o número de casos para homens.")
    st.markdown("##### Tais pontos são apoiados pelos primeiros três gráficos que mostram que não existe uma grande diferença no número de dados, tais como faixa etária e sexo, sem isso os pontos acima demonstrados poderiam estar incorretos.")
  # components.html("""<hr style="height:6px;margin-bottom: 8px;border:none;color:#ffff;background-color:#ffff;" /> """)
  components.html("""<br/> <br/>""")
  row2_space1, row2_space2 = st.columns(2)

  with row2_space1:
    st.markdown("""## Análise por doenças cardiovasculares:""")
    # st.markdown('Investigue a variedade de estatísticas para doenças cardiovasculares. Qual time marca mais gols por jogo? Como sua equipe se compara em termos de distância percorrida por jogo?')
    plot_x_heart_disease= st.selectbox ("Qual atributo você deseja analisar?", list(label_attr_dict_heart_disease.keys()), key = 'attribute_heart_disease')
    plot_x_heart_disease_type = st.selectbox ("Qual medida você deseja analisar?", types, key = 'measure_heart_disease')
  
  with row2_space2:
    plot_x_per_team(plot_x_heart_disease, plot_x_heart_disease_type)