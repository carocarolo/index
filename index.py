
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import plotly.graph_objs as go 
import altair as alt
import requests
from textblob import TextBlob
import folium
import branca.colormap as cm




data=pd.read_csv('zara.csv')
chart_data = pd.DataFrame(data)

#st.sidebar.title("Welcome Streamlitters!")


st.title('The Zara Index')
st.text('The Zara Index is a proxy to estimate in what countries fashion is more affordable and understand the difference of prices across different countries ')
st.subheader('How was this index born?')
st.text('This index was born on a trip to Venice')

geojson_url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'
response = requests.get(geojson_url)
geojson = response.json()

  
#Data for maps
map_data = data[['country_code_3', 'price_USD']]
map_data.head()

#Create Variables for scale 
min=data['price_USD'].min()
max=data['price_USD'].max()
quantile_25=data['price_USD'].quantile(0.25)
quantile_50=data['price_USD'].quantile(0.5)
quantile_75=data['price_USD'].quantile(0.75)
min1=int(round(min))
max1=int(round(max))
q25=int(round(quantile_25.item()))
q50=int(round(quantile_50.item()))
q75=int(round(quantile_75.item()))
  
#Create map 

M = folium.Map(location=[20, 10], zoom_start=1,max_bounds=True,height="%100",)

folium.Choropleth(
     geo_data=geojson,
     data=map_data,
     columns=['country_code_3', 'price_USD'],
     threshold_scale=[min1-2, q25, q50, q75,100,max1+1],
     key_on='feature.id',
     fill_color='YlGnBu',
     fill_opacity=1,
     line_opacity=0.2,
     nan_fill_color="White",
     popup=['country_code_3'],
     tooltip=['country_code_3','price_USD'],
     smooth_factor=0
).add_to(M)

#M

st_data=st_folium(M)

st.subheader('How much is this dress in every country of the world?')
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
  
  
st.title('Countries where Zara is more expensive')
chart_top10 = chart_data.nlargest(10,'price_USD')
bar_chart_top=alt.Chart(chart_top10).mark_bar().encode(
  y=alt.Y('country_name:O',sort='-x'),
  x='price_USD:Q',
)
text = bar_chart_top.mark_text(
  align='left',
  baseline='middle',
  dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
text='price_USD:Q'
)
st.altair_chart(bar_chart_top, use_container_width=True)
  
  
st.title('Countries where Zara is cheaper')
chart_bottom10 = chart_data.nsmallest(10,'price_USD')
bar_chart_bottom=alt.Chart(chart_bottom10).mark_bar().encode(
  y=alt.Y('country_name:O',sort='-x'),
  x='price_USD:Q',
)
text = bar_chart_bottom.mark_text(
  align='left',
  baseline='middle',
  dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
text='price_USD:Q'
)
st.altair_chart(bar_chart_bottom, use_container_width=True)
  