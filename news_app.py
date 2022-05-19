import requests
import pandas as pd
import json
import streamlit as st
import Altair as alt

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

#Create line graph 
line_chart = alt.Chart(df).mark_line().encode(
  x=alt.X('datetime:N'),
  y=alt.Y('close:Q'),
  color=alt.Color("name:N")
).properties(title="Hello World")
st.altair_chart(line_chart, use_container_width=True)

#Retrieve News Data 
fmt_news = f'https://eodhistoricaldata.com/api/news?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&s={ticker}'
r_news = requests.get(url)
result_news = r_news.json()

