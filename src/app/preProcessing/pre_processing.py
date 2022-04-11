import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from imblearn.under_sampling import RandomUnderSampler


ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')

providers = ds.drop(['HeartDisease'], axis=1)
classe = ds['HeartDisease']

rus = RandomUnderSampler(sampling_strategy=1)
providers_stroke_ds, classe_stroke_ds = rus.fit_resample(providers, classe)
unbalancedHistogram = px.histogram(ds, x="HeartDisease")
balancedHistogram = px.histogram(classe_stroke_ds, x="HeartDisease")




def pre_processing():

  st.title('Pré-processamento dos dados')
  st.markdown('#### Abaixo serão executados alguns procedimentos necessários para a aplicação dos algorítmos de machine learning')

  st.markdown('#### Visão geral do dataset')
  st.write(ds.head(10))


  st.title('Separação entre a classe e provisores.')
  row0_space1, row0_space2 = st.columns(2)
  with row0_space1:
    st.markdown('#### Provisores')
    st.write(providers)
  
  with row0_space2:
    st.markdown('#### Classe')
    st.write(classe)



  st.title('Balanceamento de dados.')
  row1_space1, row1_space2 = st.columns(2)
  with row1_space1:
    st.markdown('#### Dataset não balanceado.')
    st.plotly_chart(unbalancedHistogram)

  with row1_space2:
    st.markdown('#### Dataset balanceado')
    st.plotly_chart(balancedHistogram)
  


