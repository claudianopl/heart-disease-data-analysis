import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def data_exploretion(ds):
  dsOnlyHeartDiseaseYes = ds[ds['HeartDisease'] == 'Yes']

  ageOrder = ["80 or older", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "45-49","40-44", "35-39", "30-34", "25-29", "18-24"]

  histogramSexCount = px.histogram(ds, x="Sex", color="Sex",  color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})

  histogramAgeCategory = px.histogram(dsOnlyHeartDiseaseYes, x="AgeCategory", color="Sex", barmode="group", color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})
  df = px.data.tips()

  heatMap = px.density_heatmap(ds, x="AgeCategory", y="Sex", category_orders={"AgeCategory": ageOrder})

  smoking_x_HeartDisease= px.histogram(dsOnlyHeartDiseaseYes, x="HeartDisease", color="Smoking", barmode="group", color_discrete_map = {'Yes':'red','No':'blue'})

  drinking_x_HeartDisease= px.histogram(dsOnlyHeartDiseaseYes, x="HeartDisease", color="AlcoholDrinking", barmode="group", color_discrete_map = {'Yes':'red','No':'blue'})

  physicalActivity_x_HeartDisease=px.histogram(dsOnlyHeartDiseaseYes, x="HeartDisease", color="PhysicalActivity", barmode="group", color_discrete_map = {'Yes':'blue','No':'red'})

  y = ds['AgeCategory'].value_counts()
  pieChart = px.pie(y, values=y, names=y.index )
  pieChart.update_traces(textposition='inside', textinfo='percent+label')

  st.title('Análise exploratória de dados')

  st.markdown('### Seção 01: Existe alguma relação entre os  problemas cardiovasculares apresentado nos pacientes e suas características fisiológicas?')

  row0_space1, row0_space2 = st.columns(2)

  with row0_space1:
    st.markdown("#### Como está a dispersão de dados relacionados à idade no dataset?")
    st.plotly_chart(pieChart)
    st.markdown('Nota-se que a grande maioria das faixas etárias estão relativamente balanceadas, com uma maior predominância nas idades 70-74, 60-64 e 65-69.')

  with row0_space2:
    st.markdown("""#### A partir de outra perspectiva, como a idade e sexo estão dispersos no dataset?""")
    st.plotly_chart(heatMap)
    st.markdown('Percebe-se que, como antes visto, as idades 70-74, 65-69 e 60-64 estão mais presentes em ambos os gêneros, entretanto, existem mais registros do sexo feminino.')
  

  row1_space1, row2_space2 = st.columns(2)

  with row1_space1:
    st.markdown("""#### Os gêneros estão balanceados no dataset?""")
    st.plotly_chart(histogramSexCount)
    st.markdown("Nota-se que existem mais mulheres no dataset.")

  with row2_space2:
    st.markdown("""#### Agora, após filtrar o dataset para casos positivos, como esses casos se comportam em relação à idade e sexo do paciente? """)
    st.plotly_chart(histogramAgeCategory)
    st.markdown('De acordo com os gráfico é perceptível que os casos positivos começam a aumentar de forma mais notável a partir da faixa etária de 50-54 anos em ambos os sexos, é também visível que o sexo que mais possui casos é o masculino.')

  row2_space1, row2_space2 = st.columns((1.2, .8))

  with row2_space1:
    st.markdown("""### Pontos interessantess da seção 1:""")
    st.markdown(" - A idade mostrou ser um fator importante para o aumento dos casos positivos.")
    st.markdown(" - O sexo também tem um grau de relevância, tendendo aumentar o número de casos para homens.")
    st.markdown("##### Tais pontos são apoiados pelos primeiros três gráficos que mostram que não existe uma grande diferença no número de dados, tais como faixa etária e sexo, sem isso os pontos acima demonstrados poderiam estar incorretos.")

  st.markdown('### Seção 02: Existe alguma relação entre hábitos e o desenvolvimento de problemas cardiovasculares?')

  row3_space1, row3_space2 = st.columns(2)

  with row3_space1:
    st.markdown("#### O hábito de fumar gera algum impacto no desenvolvimento de problemas cardiovasculares?")
    st.plotly_chart(smoking_x_HeartDisease)
    st.markdown('O gráfico acima nos mostra que apesar da diferença não ser grande, ainda assim, os fumantes são a maioria entre os casos confirmados com problemas cardiovasculares.')

  with row3_space2:
    st.markdown("#### No gráfico abaixo veremos se o fato de consumir bebidas alcoólicas possui alguma relação com o desenvolvimento de doenças cardiovasculares.")
    st.plotly_chart(drinking_x_HeartDisease)
    st.markdown('Como podemos ver, o hábito de consumir bebidas alcoólicas não está diretamente ligado ao desenvolvimento de problemas cardiovasculares.')

  row4_space1 = st.columns(1)

  with row4_space1:
    st.markdown("#### A falta de prática de atividade fisicas pode ter alguma influencia no desenvolvimento de doenças cardiovasculares?")
    st.plotly_chart(physicalActivity_x_HeartDisease)
    st.markdown('De acordo com o gráfico acima, a falta de prática de atividades físicas não está diretamente ligada ao desenvolvimento de doenças cardiovasculares.')