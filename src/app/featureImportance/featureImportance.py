import pandas as pd
import streamlit as st
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import plot_confusion_matrix
from yellowbrick.classifier import ConfusionMatrix
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from app.preProcessing.pre_processing import ds_balancededArrayScaled_x
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction import DictVectorizer
import plotly.express as px


# def featureImportance():
#   ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')

#   fig = px.density_contour(ds, x="BMI", y="HeartDisease")

#   # py.iplot(fig, filename='histogram_subplots')
#   st.plotly_chart(fig)

#   fig = px.density_contour(ds, x="AgeCategory", y="HeartDisease")

#   # py.iplot(fig, filename='histogram_subplots')
#   st.plotly_chart(fig)


# def plot_feature_importance(importance,names,model_type):
#   #Create arrays from feature importance and feature names
#   feature_importance = np.array(importance)
#   feature_names = np.array(names)

#   #Create a DataFrame using a Dictionary
#   data={'feature_names':feature_names,'feature_importance':feature_importance}
#   fi_df = pd.DataFrame(data)

#   #Sort the DataFrame in order decreasing feature importance
#   fi_df.sort_values(by=['feature_importance'], ascending=False,inplace=True)

#   #Define size of bar plot
#   plt.figure(figsize=(10,8))
#   #Plot Searborn bar chart
#   sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])
#   #Add chart labels
#   plt.title(model_type + 'FEATURE IMPORTANCE')
#   plt.xlabel('FEATURE IMPORTANCE')
#   plt.ylabel('FEATURE NAMES')

# def featureImportance():
#   data = pd.read_csv("data/heartDiseaseNoOutlier.csv")
  
#   X = data.iloc[:,0:17]  #independent columns
#   y = data.iloc[:,17]    #target column i.e price range
#   #get correlations of each features in dataset
#   corrmat = data.corr()
#   top_corr_features = corrmat.index
#   plt.figure(figsize=(20,20))
#   #plot heat map
#   g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")

#   st.pyplot(g)

def featureImportance():
  csv = pd.read_csv("data/heartDiseaseNoOutlier.csv")
  random_forest_heartDisease = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state = 0)
  csv_clean_x = csv.drop(['HeartDisease'], axis=1)
  ds_balancedArray_x = csv.iloc[:, 0:17].values 
  ds_balancedAarray_y = csv.iloc[:, 17].values 
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

  scaler_credit = StandardScaler()

  ds_balancedArray_x_training, ds_balancedArray_x_test, ds_balancedAarray_y_training, ds_balancedAarray_y_test = train_test_split(ds_balancedArray_x, ds_balancedAarray_y, test_size = 0.25, random_state = 0)
  random_forest_heartDisease.fit(ds_balancedArray_x_training, ds_balancedAarray_y_training) 
  Importance = pd.DataFrame(random_forest_heartDisease.feature_importances_)
  address = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 'MentalHealth','DiffWalking', 'Sex','AgeCategory', 'Race','Diabetic', 'PhysicalActivity','Genhealth', 'SleepTime','Asthma', 'KidneyDisease','SkinCancer']
  Importance['Variables'] = address
  Importance = Importance.rename(columns = {0:'Feature importance'})
  Importance = Importance.sort_values(by=['Feature importance'], ascending=True)

  featureImportanceHistgram = px.histogram(Importance, x="Variables", y="Feature importance")
  st.markdown('#### Dataframe da feature importance')
  st.write(Importance)
  st.markdown('#### Abaixo uma representação gráfica das feature importances')
  st.plotly_chart(featureImportanceHistgram)

