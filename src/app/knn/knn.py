import streamlit as st
import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import plot_confusion_matrix, classification_report
import pickle
from yellowbrick.classifier import ConfusionMatrix


try:
  KNN_heartDisease = joblib.load("pipeline/jobs/knn.joblib")
  with open('data\ds_balanced_No_Outlier_PKL.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  previsoes = KNN_heartDisease.predict(ds_heartDisease_x_test)
  # Aplicando matriz de confusão
  cm = ConfusionMatrix(KNN_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)
  
except:
  with open('data\ds_balanced_No_Outlier_PKL.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  KNN_heartDisease = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)
  KNN_heartDisease.fit(ds_heartDisease_x_training, ds_heartDisease_y_training)

  joblib.dump(KNN_heartDisease, "pipeline/jobs/knn.joblib")

  previsoes = KNN_heartDisease.predict(ds_heartDisease_x_test)

  # Aplicando matriz de confusão
  cm = ConfusionMatrix(KNN_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)


def MLKNN():    
  st.markdown("#### Aplicando KNN, com tratamento do outline.")

  st.write('Acuracia: ', acc)

  row1_space1, row1_space2 = st.columns((2))
  with row1_space1:
    st.markdown("#### Matriz de confusão com outlier tratado:")
    plot_confusion_matrix(KNN_heartDisease, ds_heartDisease_x_test, ds_heartDisease_y_test)  
    st.pyplot()
  
  with row1_space2:
    st.markdown("#### Classification report: apenas 25% dos dados totais")
    classificationReport = classification_report(ds_heartDisease_y_test, previsoes,  output_dict=True)
    classificationReportDataFrame = pd.DataFrame(classificationReport).transpose()
    st.write(classificationReportDataFrame)