import requests
import pandas as pd
import json
import streamlit as st
import altair as alt
from pyspark.conf import SparkConf
from pyspark import SparkContext
from pyspark.sql import SQLContext

ticker=st.selectbox('Select ticker',('AAPL','EC'))
st.write('You selected:', ticker)
btn=st.button('Buscar')

#Establishing URL parameters
url = f"https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&apikey=demo&source=docs"

#Retrieving data from Website
r = requests.get(url)
result = r.json()

aapl = result['values']
df=pd.DataFrame(aapl)

y_data_max = df['close'].max()
y_data_min = df['close'].min()

#Create line graph 
line_chart = alt.Chart(df).mark_line().encode(
  x=alt.X('datetime:N'),
  y=alt.Y('close:Q', scale=alt.Scale(domain=(y_data_min, y_data_max )))
).properties(title="Hello World") #Agregar Titulo dependiendo del valor de ticker
st.altair_chart(line_chart, use_container_width=True)

#Retrieve News Data 
fmt_news = f'https://eodhistoricaldata.com/api/news?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&s={ticker}'
r_news = requests.get(url)
result_news = r_news.json()

