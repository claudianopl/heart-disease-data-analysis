import streamlit as st
import pandas as pd
import joblib
from sklearn.svm import SVC
from sklearn.metrics import plot_confusion_matrix, classification_report
import pickle
from yellowbrick.classifier import ConfusionMatrix


try:
  SVM_heartDisease = joblib.load("pipeline/jobs/svm.joblib")
  with open('data\ds_balanced_No_Outlier_PKL.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  predictions = SVM_heartDisease.predict(ds_heartDisease_x_test)

  # Aplicando matriz de confusão
  cm = ConfusionMatrix(SVM_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)
except:
  with open('data\ds_balanced_No_Outlier_PKL.pkl', 'rb') as f:  
    ds_heartDisease_x_training, ds_heartDisease_y_training , ds_heartDisease_x_test, ds_heartDisease_y_test = pickle.load(f)

  SVM_heartDisease = SVC(kernel='linear', random_state=1, C = 2.0)
  SVM_heartDisease.fit(ds_heartDisease_x_training, ds_heartDisease_y_training)

  joblib.dump(SVM_heartDisease, "pipeline/jobs/svm.joblib")

  predictions = SVM_heartDisease.predict(ds_heartDisease_x_test)

  # Aplicando matriz de confusão
  cm = ConfusionMatrix(SVM_heartDisease)
  acc  = cm.score(ds_heartDisease_x_test, ds_heartDisease_y_test)


def MLSVM():    
  st.markdown("#### Aplicando SVM, com tratamento do outline.") 

  st.write('Acuracia: ', acc)

  row1_space1, row1_space2 = st.columns((2))
  with row1_space1:
    st.markdown("#### Matriz de confusão com outlier tratado:")
    plot_confusion_matrix(SVM_heartDisease, ds_heartDisease_x_test, ds_heartDisease_y_test)  
    st.pyplot()
 
  with row1_space2:
    st.markdown("#### Classification report: apenas 25% dos dados totais")
    classificationReport = classification_report(ds_heartDisease_y_test, predictions,  output_dict=True)
    classificationReportDataFrame = pd.DataFrame(classificationReport).transpose()
    st.write(classificationReportDataFrame)