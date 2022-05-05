from numpy import sort
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from app.home.home import Home
from app.dataExploration.data_exploration import data_exploration
from app.preProcessing.pre_processing import pre_processing
from app.randomForest.randomForest import randomForest
from app.outlier.outlier import outlier
from app.randomForestWithoutOutlier.randomForestWithoutOutlier import randomForestWithoutOutlier


ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')


optionsDict = {
  'Página Inicial': 'home',
  'Analise exploratória': 'exploratoryAnalysis',
  'Pré-processamento': 'preProcessing',
  'Outlier': 'outlier',
  'Random-Forest': 'randomForest',
  'Random-Forest com outlier tratado': 'randomForestWithoutOutlier'
}

st.set_page_config(layout="wide")
with st.sidebar:
  selected = option_menu(
    menu_title='Menu Principal',
    options=['Página Inicial', 'Pré-processamento', 'Outlier', 'Analise exploratória', 'Random-Forest', 'Random-Forest com outlier tratado'],
    icons=['house-door-fill', 'gear-fill', 'align-top', 'bar-chart-fill', 'bezier', 'bezier'],
    menu_icon='cast',
    default_index=0,
  )
st.set_option('deprecation.showPyplotGlobalUse', False)
options = optionsDict[selected]
if options == 'home':
  Home()
if options == 'preProcessing':
  pre_processing()
if options == 'outlier':
  outlier()
if options == 'exploratoryAnalysis':
  data_exploration()
if options == 'randomForest':
  randomForest()
if options == 'randomForestWithoutOutlier':
  randomForestWithoutOutlier()
