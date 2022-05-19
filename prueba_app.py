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


st.sidebar.title("Welcome Streamlitters!")


with header: 
  st.title('The Zara Index')
  st.text('The Zara Index is a proxy to estimate in what countries fashion is more affordable and understand the difference of prices across different countries ')
  st.subheader('How was this index born?')
  st.text('This index was born on a trip to Venice')

  
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
  st.title('Countries where Zara is more expensive')
  chart_top10 = chart_data.nlargest(10,'price_USD')
  bar_chart=alt.Chart(chart_top10).mark_bar().encode(
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
  
  
with bottom10:
  st.title('Countries where Zara is cheaper')
  chart_top10 = chart_data.nsmallest(10,'price_USD')
  
  
