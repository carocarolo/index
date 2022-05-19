import requests
import pandas as pd
import json
import streamlit as st
import pycountry

#Establishing URL parameters
fmt = 'https://api.twelvedata.com/time_series?symbol={ticker}&interval={interval}&apikey={apikey}&source=docs'
values = { 'apikey': 'demo', 'ticker': 'AAPL','interval':'1day' }
url=fmt.format(**values)
#print(url)

#Retrieving data from Website
r = requests.get(url)
result = r.json()
print (type(result).__name__)
print(result)


