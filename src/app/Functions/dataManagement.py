import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

#csvToPickle(ds_balanced, 'picre')
def csvToPickle(csv,name):
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
  oneHotEnconderColumnTarget = [1,2,3,6,7,8,9,10,11,12,14,15,16]
  oneHotEncoder = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), oneHotEnconderColumnTarget)], remainder='passthrough')
  scaler_credit = StandardScaler()
  ds_balancededArrayEncoded_x = oneHotEncoder.fit_transform(ds_balancedArray_x)
  ds_balancededArrayScaled_x = scaler_credit.fit_transform(ds_balancededArrayEncoded_x)
  ds_balancedArray_x_training, ds_balancedArray_x_test, ds_balancedAarray_y_training, ds_balancedAarray_y_test = train_test_split(ds_balancededArrayScaled_x, ds_balancedAarray_y, test_size = 0.25, random_state = 0)
  with open('data/{}.pkl'.format(name), mode = 'wb') as f:
    pickle.dump([ds_balancedArray_x_training, ds_balancedAarray_y_training, ds_balancedArray_x_test, ds_balancedAarray_y_test], f)

