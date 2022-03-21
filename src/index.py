from numpy import sort
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from dataExploretion.data_exploretion import data_exploretion

ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')

optionsDict = {
  'Analise exploratória': 'exploratoryAnalysis',
  'Pré-processamento': 'preProcessing'
}

st.set_page_config(layout="wide")
with st.sidebar:
  selected = option_menu(
    menu_title='Menu Principal',
    options=['Pré-processamento', 'Analise exploratória'],
    icons=['gear-fill', 'bar-chart-fill'],
    menu_icon='cast',
    default_index=0,
  )

options = optionsDict[selected]
if options == 'preProcessing':
  st.title('Pré-processamento dos dados')
if options == 'exploratoryAnalysis':
  data_exploretion(ds)
