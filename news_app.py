import requests
import pandas as pd
import json
import streamlit as st

ticker=st.selectbox('Select ticker',('AAPL','EC'))
st.write('You selected:', ticker)
btn=st.button('Buscar')

#Establishing URL parameters
if btn:
  fmt = f'https://api.twelvedata.com/time_series?symbol={ticker}&interval=1day&apikey=demo&source=docs'

#Retrieving data from Website
r = requests.get(url)
result = r.json()

aapl = result['values']
pt=pd.DataFrame(aapl)


#Retrieve News Data 
fmt_news = f'https://eodhistoricaldata.com/api/news?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&s={ticker}'
r_news = requests.get(url)
result_news = r_news.json()

