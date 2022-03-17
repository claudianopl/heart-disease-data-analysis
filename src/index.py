from numpy import sort
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

ds = pd.read_csv('D:\Projetos\dataStackPisi3\heart-disease-data-analysis\data\personal-key-indicators-of-heart-disease-dataset.csv')

# ds
# x = ds.drop(['HeartDisease'], axis=1)
# y = ds['HeartDisease']

# ax = y.value_counts().plot.pie(autopct='%.2f')
# _ = ax.set_title("Under-sampling")

st.write("""
# My first app
Hello *world!*
""")

st.title('É possível existir alguma relação dos problemas cardiovasculares apresentado nos pacientes com as características fisiológicas de um indivíduo como, idade, sexo, doenças e seu IMC?')


dsOnlyHeartDiseaseYes = ds[ds['HeartDisease'] == 'Yes']



ageOrder = ["80 or older", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "45-49","40-44", "35-39", "30-34", "25-29", "18-24"]

histogramSexCount = px.histogram(ds, x="Sex", color="Sex", title='Quantidade de homens e mulheres no dataset', color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})

histogramAgeCategory = px.histogram(dsOnlyHeartDiseaseYes, x="AgeCategory", color="Sex", barmode="group", title='Demonstração dos casos positivos, de acordo com idade, gênero e faixa etária', color_discrete_map = {'Male':'blue','Female':'red'}, category_orders={"AgeCategory": ageOrder})
df = px.data.tips()

heatMap = px.density_heatmap(ds, x="AgeCategory", y="Sex", category_orders={"AgeCategory": ageOrder})

y = ds['AgeCategory'].value_counts()
y
pieChart = px.pie(y, values=y, names=y.index ,title='Dispersão de idade no dataset')
pieChart.update_traces(textposition='inside', textinfo='percent+label')

st.plotly_chart(pieChart)
st.plotly_chart(heatMap)
st.plotly_chart(histogramSexCount)
st.plotly_chart(histogramAgeCategory)



