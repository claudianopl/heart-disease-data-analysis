import pandas as pd
import streamlit as st
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import plot_confusion_matrix
from yellowbrick.classifier import ConfusionMatrix

try:
  random_forest_heartDisease = joblib.load("pipeline/jobs/random_forest_without_outlier.joblib")
  with open('data\ds_balanced_No_Outlier_PKL.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  predictions = random_forest_heartDisease.predict(ds_heartDisease_x_test)

  # Aplicando matriz de confusão
  cm = ConfusionMatrix(random_forest_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)
except:
  with open('data\ds_balanced_No_Outlier_PKL.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  random_forest_heartDisease = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state = 0)
  random_forest_heartDisease.fit(ds_heartDisease_x_training, ds_heartDisease_y_training)
  
  joblib.dump(random_forest_heartDisease, "pipeline/jobs/random_forest_without_outlier.joblib")

  predictions = random_forest_heartDisease.predict(ds_heartDisease_x_test)

  # Aplicando matriz de confusão
  cm = ConfusionMatrix(random_forest_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)

def randomForestWithoutOutlier():#essa função vai servir apenas para mostrar o resultado do machine learning em tela
  st.markdown("### Aplicando randomForest, com tratamento do outline.")

  st.write('Acuracia: ', acc)

  row1_space1, row1_space2 = st.columns((2))
  with row1_space1:
    st.markdown("#### Matriz de confusão com outlier tratado:")
    plot_confusion_matrix(random_forest_heartDisease, ds_heartDisease_x_test, ds_heartDisease_y_test)  
    st.pyplot()
  
  with row1_space2:
    st.markdown("#### Classification report: apenas 25% dos dados totais")

    classificationReport = classification_report(ds_heartDisease_y_test, predictions,  output_dict=True)
    classificationReportDataFrame = pd.DataFrame(classificationReport).transpose()
    st.write(classificationReportDataFrame)


