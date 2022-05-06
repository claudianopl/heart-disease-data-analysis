import pandas as pd
import streamlit as st
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import plot_confusion_matrix
from yellowbrick.classifier import ConfusionMatrix


try:
  random_forest_heartDisease = joblib.load("pipeline/jobs/random_forest.joblib")
  with open('data/heartDisease.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  predictions = random_forest_heartDisease.predict(ds_heartDisease_x_test)

  # Aplicando matriz de confusão
  cm = ConfusionMatrix(random_forest_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)
except:
  preProcessedDataset = pd.read_pickle(r'data/heartDisease.pkl')

  with open('data/heartDisease.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  random_forest_heartDisease = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state = 0)
  random_forest_heartDisease.fit(ds_heartDisease_x_training, ds_heartDisease_y_training)

  joblib.dump(random_forest_heartDisease, "pipeline/jobs/random_forest.joblib")

  predictions = random_forest_heartDisease.predict(ds_heartDisease_x_test)

  
  # Aplicando matriz de confusão
  cm = ConfusionMatrix(random_forest_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)

  



def randomForest():#essa função vai servir apenas para mostrar o resultado do machine learning em tela
  st.markdown("### Aplicando randomForest, sem tratar o Outline.")

  st.write('Acuracia: ', acc)

  row1_space1, row1_space2 = st.columns((2))
  with row1_space1:
    st.markdown("#### Matriz de confusão:")
    plot_confusion_matrix(random_forest_heartDisease, ds_heartDisease_x_test, ds_heartDisease_y_test)  
    st.pyplot()



