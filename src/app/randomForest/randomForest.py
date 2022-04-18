import pandas as pd
import streamlit as st
import pickle


preProcessedDataset = pd.read_pickle(r'data/heartDisease.pkl')

with open('heartDisease.pkl', 'rb') as f:  
  ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

#codigo bruto vem acima

def randomForest():#essa função vai servir apenas para mostrar o resultado do machine learning em tela
  st.write(preProcessedDataset)#pode apagar se quiser