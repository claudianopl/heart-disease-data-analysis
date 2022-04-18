import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pickle
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')

providers = ds.drop(['HeartDisease'], axis=1)
classe = ds['HeartDisease']

rus = RandomUnderSampler(sampling_strategy=1)

providers_ds, classe_ds = rus.fit_resample(providers, classe)
unbalancedHistogram = px.histogram(ds, x="HeartDisease")
balancedHistogram = px.histogram(classe_ds, x="HeartDisease")

ds_balanced = pd.concat([providers_ds, classe_ds], axis=1)
ds_balancedArray_x = ds_balanced.iloc[:, 0:17].values #0:17 = previsores o 18 é a classe que não está inclusa aqui
ds_balancedAarray_y = ds_balanced.iloc[:, 17].values #classe

le = LabelEncoder()

label_encoder_smoking = LabelEncoder()
label_encoder_AlcoholDrinking = LabelEncoder()
label_encoder_Stroke = LabelEncoder()
label_encoder_DiffWalking = LabelEncoder()
label_encoder_Sex = LabelEncoder()
label_encoder_AgeCategory = LabelEncoder()
label_encoder_Race = LabelEncoder()
label_encoder_Diabetic = LabelEncoder()
label_encoder_PhysicalActivity = LabelEncoder()
label_encoder_GenHealth = LabelEncoder()
label_encoder_Asthma	= LabelEncoder()
label_encoder_KidneyDisease = LabelEncoder()
label_encoder_SkinCancer = LabelEncoder()



ds_balancedArray_x[:,1] = label_encoder_smoking.fit_transform(ds_balancedArray_x[:,1])
ds_balancedArray_x[:,2] = label_encoder_AlcoholDrinking.fit_transform(ds_balancedArray_x[:,2])
ds_balancedArray_x[:,3] = label_encoder_Stroke.fit_transform(ds_balancedArray_x[:,3])
ds_balancedArray_x[:,6] = label_encoder_DiffWalking.fit_transform(ds_balancedArray_x[:,6])
ds_balancedArray_x[:,7] = label_encoder_Sex.fit_transform(ds_balancedArray_x[:,7])

ds_balancedArray_x[:,8] = label_encoder_AgeCategory.fit_transform(ds_balancedArray_x[:,8])
ds_balancedArray_x[:,9] = label_encoder_Race.fit_transform(ds_balancedArray_x[:,9])
ds_balancedArray_x[:,10] = label_encoder_Diabetic.fit_transform(ds_balancedArray_x[:,10])
ds_balancedArray_x[:,11] = label_encoder_PhysicalActivity.fit_transform(ds_balancedArray_x[:,11])
ds_balancedArray_x[:,12] = label_encoder_GenHealth.fit_transform(ds_balancedArray_x[:,12])
ds_balancedArray_x[:,14] = label_encoder_Asthma.fit_transform(ds_balancedArray_x[:,14])
ds_balancedArray_x[:,15] = label_encoder_KidneyDisease.fit_transform(ds_balancedArray_x[:,15])
ds_balancedArray_x[:,16] = label_encoder_SkinCancer.fit_transform(ds_balancedArray_x[:,16])

oneHotEnconderColumnTarget = [1,2,3,6,7,8,9,10,11,12,14,15,16]
oneHotEncoder = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), oneHotEnconderColumnTarget)], remainder='passthrough')
scaler_credit = StandardScaler()

ds_balancededArrayEncoded_x = oneHotEncoder.fit_transform(ds_balancedArray_x)

ds_balancededArrayScaled_x = scaler_credit.fit_transform(ds_balancededArrayEncoded_x)


ds_balancedArray_x_training, ds_balancedArray_x_test, ds_balancedAarray_y_training, ds_balancedAarray_y_test = train_test_split(ds_balancededArrayScaled_x, ds_balancedAarray_y, test_size = 0.25, random_state = 0)

with open('heartDisease.pkl', mode = 'wb') as f:
  pickle.dump([ds_balancedArray_x_training, ds_balancedAarray_y_training, ds_balancedArray_x_test, ds_balancedAarray_y_test], f)

def pre_processing():

  st.title('Pré-processamento dos dados')
  st.markdown('#### Abaixo serão executados alguns procedimentos necessários para a aplicação dos algorítmos de machine learning')

  st.markdown('#### Visão geral do dataset')
  st.write(ds.head(10))


  st.title('Separação entre a classe e previsores.')
  row0_space1, row0_space2 = st.columns(2)
  
  st.markdown('#### Previsores')
  st.write(providers)
  
  
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
  

  st.title('Aplicação do label encoder.')
  row2_space1 = st.columns(1)
  st.markdown('#### previsores')
  st.write(ds_balancedArray_x)#previsores
  st.markdown('#### classe')
  st.write(ds_balancedAarray_y)#classe

  st.title('Aplicando o oneHotEncoder')
  st.write(ds_balancededArrayEncoded_x)

  st.title('Escalonamento dos previsores')
  st.write(ds_balancededArrayScaled_x)

  st.markdown('Foram separados 75% dos dados para treinamento e 25% para testes')
  st.markdown('##### Quantidade de registros de treinamento:')  
  st.write(ds_balancedArray_x_training.shape)
  st.markdown('##### Quantidade de registros de teste:')
  st.write(ds_balancedArray_x_test.shape)

  st.markdown('## Agora os dados estão prontos para serem usados por algum algoritmo de machine learning')


