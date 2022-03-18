from numpy import sort
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit.components.v1 as components

ds = pd.read_csv('D:\Projetos\dataStackPisi3\heart-disease-data-analysis\data\personal-key-indicators-of-heart-disease-dataset.csv')


st.title('Análise exploratória de dados')



dsOnlyHeartDiseaseYes = ds[ds['HeartDisease'] == 'Yes']

ageOrder = ["80 or older", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "45-49","40-44", "35-39", "30-34", "25-29", "18-24"]

histogramSexCount = px.histogram(ds, x="Sex", color="Sex",  color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})

histogramAgeCategory = px.histogram(dsOnlyHeartDiseaseYes, x="AgeCategory", color="Sex", barmode="group", color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})
df = px.data.tips()

heatMap = px.density_heatmap(ds, x="AgeCategory", y="Sex", category_orders={"AgeCategory": ageOrder})

y = ds['AgeCategory'].value_counts()
pieChart = px.pie(y, values=y, names=y.index )
pieChart.update_traces(textposition='inside', textinfo='percent+label')

st.markdown("""
## Seção 1:
## Existe alguma relação entre os  problemas cardiovasculares apresentado nos pacientes e suas características fisiológicas?
### 
""")

st.markdown("""
### Como está a dispersão de dados relacionados à idade no dataset ?
""")
st.plotly_chart(pieChart)
st.markdown("""
#### Nota-se que a grande maioria das faixas etárias estão relativamente balanceadas, com uma maior predominância nas idades 70-74, 60-64 e 65-69.
""")
components.html("""<hr style="height:6px;border:none;color:#ffff;background-color:#ffff;" /> """)

st.markdown("""
### A partir de outra perspectiva, como a idade e sexo estão dispersos no dataset?
""")
st.plotly_chart(heatMap)
st.markdown("""
#### Percebe-se que, como antes visto, as idades 70-74, 65-69 e 60-64 estão mais presentes em ambos os gêneros, entretanto, existem mais registros do sexo feminino.
""")
components.html("""<hr style="height:6px;border:none;color:#ffff;background-color:#ffff;" /> """)

st.markdown("""
### Os gêneros estão balanceados no dataset ?
""")
st.plotly_chart(histogramSexCount)
st.markdown("""
#### Nota-se que existem mais mulheres no dataset.
""")
components.html("""<hr style="height:6px;border:none;color:#ffff;background-color:#ffff;" /> """)

st.markdown("""
### Agora, apos filtrar o dataset para casos positivos, como esses casos se comportam em relação à idade e sexo do paciente? """)
st.plotly_chart(histogramAgeCategory)
st.markdown("""
#### De acordo com os gráfico é perceptível que os casos positivos começam a aumentar de forma mais notável a partir da faixa etária de 50-54 anos em ambos os sexos, é também visível que o sexo que mais possui casos é o masculino.
 """)
components.html("""<hr style="height:6px;border:none;color:#ffff;background-color:#ffff;" /> """)

st.markdown("""
## Pontos interessantess da seção 1:
### 1- A idade mostrou ser um fator importante para o aumento dos casos positivos.
### 2- O sexo também tem um grau de relevância, tendendo aumentar o número de casos para homens.

#### 3- Nota: Tais pontos são apoiados pelos primeiros três gráficos que mostram que não existe uma grande diferença no número de dados, tais como faixa etária e sexo, sem isso os pontos acima demonstrados poderiam estar incorretos.
# """)



