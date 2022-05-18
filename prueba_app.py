import streamlit as st
import pandas as pd
#import plotly.express as px 
import altair as alt


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
  data=pd.read_csv('zara.csv')
  st.write(data.head(20))
  
  dataframe=pd.DataFrame(data)
  
  chart_data = pd.DataFrame(['Price_USD', 'country_name'])
  bar_chart=alt.Chart(chart_data).mark_bar().encode(
    y='Price_USD',
    x='country_name',
  )
  st.altair_chart(bar_chart,use_container_width=free)
  
  
with features:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
with modelTraining:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
