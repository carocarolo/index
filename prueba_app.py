import streamlit as st
import pandas as pd

header = st.beta_container()
dataset=st.beta_container()
features=st.beta_container()
modelTraining=st.beta_container()

with header: 
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
with dataset: 
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  data=pd.read_csv('C:/Users/Carolina Mendoza/Documents/Applied Analytics/Proyectos/zara.csv')
  
with features:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
with modelTraining:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
