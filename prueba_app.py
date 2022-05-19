import streamlit as st
import pandas as pd
#import plotly.express as px 
import altair as alt
#import folium
import requests


header = st.container()
all_countries=st.container()
top10=st.container()
bottom10=st.container()
sidebar=st.sidebar()

with header: 
  st.title('The Zara Index')
  st.text('The Zara Index is a proxy to estimate in what countries fashion is more affordable and understand the difference of prices across different countries ')
  st.subheader('How was this index born?')
  st.text('This index was born on a trip to Venice')

with sidebar:
    my_component(greeting="hello")
  
with all_countries: 
  st.subheader('How much is this dress in every country of the world?')
  data=pd.read_csv('zara.csv')
  chart_data = pd.DataFrame(data)
  bar_chart=alt.Chart(chart_data).mark_bar().encode(
    y=alt.Y('country_name:O',sort='-x'),
    x='price_USD:Q',
  )
  text = bar_chart.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='price_USD:Q'
)
  st.altair_chart(bar_chart, use_container_width=True)
  
  
with top10:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  st.markdown('* **first feature:**I created this ')
  st.markdown('* **second feature:**I created this ')
  
with bottom10:
  st.title('Welcome to my life project')
  st.text('In this project I look into transactions')
  
  sel_col,disp_col=st.beta_columns(2)
  max_depth=sel_col.slider('What is the max_depth', min_value=10,max_value=100,value=20,step=10)
  n_estimators=sel_col.selectbox('How many trees should there be?',options=(100,200,300,'No limit'), index=0)
  input_feature=sel_col.text_input('Which feature should be used','PULocationID')
  
