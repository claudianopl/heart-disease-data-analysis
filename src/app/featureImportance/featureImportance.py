import pandas as pd
import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import plotly.express as px
from app.featureImportance.featureImportanceManagement import labelEncodeFeatureImportanceCSV, getFeatureImportanceGraph, createFeatureImportanceJobLibDataSet



def featureImportance():
  ds_balancedArray_x_training, ds_balancedAarray_y_training = labelEncodeFeatureImportanceCSV()  
  createFeatureImportanceJobLibDataSet(ds_balancedArray_x_training, ds_balancedAarray_y_training, 0)

  Importance, featureImportanceHistgram = getFeatureImportanceGraph("src/app/featureImportance/jobs/randomForestFI.joblib")

  row1_space1, row1_space2 = st.columns((2))
  with row1_space1:
    st.markdown('### Random Forest')
    st.markdown('#### Dataframe da feature importance')
    st.write(Importance)
    st.markdown('#### Abaixo uma representação gráfica das feature importances')
    st.plotly_chart(featureImportanceHistgram)
  