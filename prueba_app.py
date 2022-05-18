import streamlit as st
import pandas as pd
#import plotly.express as px 
import altair as alt


header = st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()

with header: 
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
with dataset: 
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  data=pd.read_csv('zara.csv')
  st.write(data.head(20))
  
  st.subheader('This is a subheader')
  chart_data = pd.DataFrame(data)
  st.write(chart_data.head(20))
  bar_chart=alt.Chart(chart_data).mark_bar().encode(
    y='price_USD:Q',
    x='country_name:O',
  )
  st.altair_chart(bar_chart, use_container_width=True)
  
  
with features:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  st.markdown('* **first feature:**I created this ')
  st.markdown('* **second feature:**I created this ')
  
with modelTraining:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
  sel_col,disp_col=st.beta_columns(2)
  max_depth=sel_col.slider('What is the max_depth', min_value=10,max_value=100,value=20,step=10)
  n_estimators=sel_col.selectbox('How many trees should there be?',options=(100,200,300,'No limit'), index=0)
  input_feature=sel_col.text_input('Which feature should be used','PULocationID')
  
