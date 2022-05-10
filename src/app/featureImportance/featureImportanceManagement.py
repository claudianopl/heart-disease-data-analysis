import pandas as pd
import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


def labelEncodeFeatureImportanceCSV():
  csv = pd.read_csv("data/heartDiseaseNoOutlier.csv")
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

  ds_balancedArray_x_training, ds_balancedArray_x_test, ds_balancedAarray_y_training, ds_balancedAarray_y_test = train_test_split(ds_balancedArray_x, ds_balancedAarray_y, test_size = 0.25, random_state = 0)

  return ds_balancedArray_x_training, ds_balancedAarray_y_training


def getFeatureImportanceGraph(jobLibDataSetPath):
  jobLibDataset = joblib.load(jobLibDataSetPath)
  Importance = pd.DataFrame(jobLibDataset.feature_importances_)
  address = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 'MentalHealth','DiffWalking', 'Sex','AgeCategory', 'Race','Diabetic', 'PhysicalActivity','Genhealth', 'SleepTime','Asthma', 'KidneyDisease','SkinCancer']
  Importance['Variables'] = address
  Importance = Importance.rename(columns = {0:'Feature importance'})
  Importance = Importance.sort_values(by=['Feature importance'], ascending=True)

  featureImportanceHistgram = px.histogram(Importance, x="Variables", y="Feature importance")

  return Importance, featureImportanceHistgram

def createFeatureImportanceJobLibDataSet(ds_balancedArray_x_training, ds_balancedAarray_y_training, MachineLearningType):
  if MachineLearningType == 0:
    machineLearningAlgorithm = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state = 0)
    algorithmName = 'RandomForestFI'
  elif MachineLearningType == 1:
    machineLearningAlgorithm = SVC(kernel='linear', random_state=1, C = 2.0)
    algorithmName = 'SVMFI'
  elif MachineLearningType == 2:
    machineLearningAlgorithm = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)
    algorithmName = 'KNNFI'
  machineLearningAlgorithm.fit(ds_balancedArray_x_training, ds_balancedAarray_y_training) 
  joblib.dump(machineLearningAlgorithm, "src/app/featureImportance/jobs/{}.joblib".format(algorithmName))



  