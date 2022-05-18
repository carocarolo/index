##pip install requests-html

import time
import re
import requests
#from resquests_html import HTMLSession
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import pycountry

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36' 
}

countrylinks=['ad','ae','al','am','az','ba','be','bg','bh','ca','ch','cn','co','cr','cy','cz','de','dk','do','dz','ee','eg','es','fi','fr','ge','gr','gt','hk','hn','hr','hu','id','ie','il','in','is','it','jo','jp','kr','kw','kz','lb','lt','lu','lv','ma','mc','me','mk','mo','mt','mx','my','nl','no','om','pa','ph','pl','pt','qa','ro','rs','ru','sa','se','sg','si','sk','sv','th','tn','tr','tw','ua','uk','us']

def build_url(country):
    return 'https://www.zara.com/'+country+'/en/linen-blend-print-dress-p03274740.html?v1=171726299'

country_urls = [build_url(country) for country in countrylinks]
print(country_urls)

dresslist=[]
for url in country_urls:
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,'lxml')
    name=soup.find('h1',class_='product-detail-info__header-name').text.strip()
    price=soup.find('span',class_='price-current__amount').text.strip()
    dress={
    'name': name,
    'price':price
    }
    dresslist.append(dress)
    print('Saving:',dress['name'])
    
df=pd.DataFrame(dresslist)
print(df.head(15))

alpha_2=countrylinks

for i in range(len(alpha_2)):
    alpha_2[i] = alpha_2[i].upper()

print(alpha_2)

for i in range(len(alpha_2)):
    if alpha_2[i] == 'UK':
        alpha_2[i] = 'GB'

countries = {}
for country in pycountry.countries:
    countries[country.alpha_2] = country.name

country_name = [countries.get(country, 'Unknown code') for country in alpha_2]

countries_code_3 = {}
for country in pycountry.countries:
    countries_code_3[country.alpha_2] = country.alpha_3

codes_3 = [countries_code_3.get(country, 'Unknown code') for country in alpha_2]
print(codes_3)

currencies=['EUR','AED','ALL','AMD','AZN','BAM','EUR','BGN','BHD','CAD','CHF','CNY','COP','CRC','EUR','CZK','EUR','DKK','DOP','DZD','EUR','EGP','EUR','EUR','EUR','GEL','EUR','GTQ','HKD','HNL','HRK','HUF','IDR','EUR','ILS','INR','ISK','EUR','JOD','JPY','KRW','KWD','KZT','LBP','EUR','EUR','EUR','MAD','EUR','EUR','MKD','MOP','EUR','MXN','MYR','EUR','NOK','OMR','PAB','PHP','PLN','EUR','QAR','RON','RSD','RUB','SAR','SEK','SGD','EUR','EUR','USD','THB','TND','TRY','TWD','UAH','GBP','USD']

df['country_name']=country_name

df['country_code']=alpha_2

df['country_code_3']=codes_3

df['currency']=currencies

df['date']= np.datetime64('2022-05-02')

df['coleccion']='Spring2022'

df['realprice'] = df['price'].astype(str)

df['itemprice'] = df['realprice'].str.extract('(\d[\d,.]*)', expand=False).str.strip()

df.itemprice = df.itemprice.apply(lambda x : x.replace(',',''))

df['itemprice'] = pd.to_numeric(df['itemprice'])

pd.set_option("display.max_rows", None, "display.max_columns", None)

#!pip install pycountry

#!pip install forex_python

df['itemprice'] = df['itemprice'].astype('int')

df['date'] = df['date'].astype('datetime64[ns]')

df['itemprice'] = pd.to_numeric(df['itemprice'])

import requests

# Where USD is the base currency you want to use

url = 'https://openexchangerates.org/api/historical/2022-05-02.json?app_id=79098365fb7c423ebe0c094b93b9788e'


# Making our request
response = requests.get(url)
data = response.json()

rates=(data['rates'])
print(rates)

pt = pd.DataFrame(list(rates.items()),columns = ['currency','rate']) 
print(pt)

df=df.merge(pt, on='currency', how='left')
df['price_USD']=df['itemprice']/df['rate']


geojson_url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'
response = requests.get(geojson_url)
geojson = response.json()
geojson['features'][0]


map_data = df[['country_code_3', 'price_USD']]
map_data.head()

#!pip install folium

import folium
M = folium.Map(location=[20, 10], zoom_start=2)


folium.Choropleth(
    geo_data=geojson,
    data=map_data,
    columns=['country_code_3', 'price_USD'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    popup=['country_code_3'],
    tooltip=['country_code_3','price_USD'],
).add_to(M)

M

#!pip install branca

import branca.colormap as cmp

step = cmp.StepColormap(
 ['yellow', 'green', 'purple'],
 vmin=3, vmax=10,
 index=[3, 6, 8, 10],  #for change in the colors, not used fr linear
 caption='Color Scale for Map'    #Caption for Color scale or Legend
)
step

import requests
import pandas as pd
import pymongo

import branca.colormap as cmp
linear = cmp.LinearColormap(
    ['yellow', 'green', 'purple'],
    vmin=minprice, vmax=maxprice,
    caption='Color Scale for Map' #Caption for Color scale or Legend
)
linear

df_dict = df.set_index('country_code_3')['price_USD']
#geo_json_data = json.loads(requests.get(state_geo).text)
usa_linear = folium.Map([48,-102], tiles='cartodbpositron', zoom_start=3)
folium.GeoJson(
    geojson,
    style_function=lambda feature: {
        'fillColor': linear(df_dict[feature['country_code']]),
        'color': 'black',     #border color for the color fills
        'weight': 1,          #how thick the border has to be
        'dashArray': '5, 3'  #dashed lines length,space between them
    }
).add_to(usa_linear)
linear.add_to(usa_linear)   #adds colorscale or legend
usa_linear

#!pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(20,12))

sns.set()
sns.barplot(
    x='price_USD', 
    y='country_name', 
    color='salmon', 
    data=df,
    order=df.sort_values('price_USD', ascending = False).country_name
)

# set labels
plt.xlabel("Price USD", size=10)
plt.ylabel("Country", size=10)
plt.title("All countries", size=18)
plt.tight_layout()

top10=df.nlargest(10,'price_USD')
bottom10=df.nsmallest(10,'price_USD')

plt.figure(figsize=(20,12))

sns.set()
sns.barplot(
    x='price_USD', 
    y='country_name', 
    color='salmon', 
    data=top10,
    order=top10.sort_values('price_USD', ascending = False).country_name
)

# set labels
plt.xlabel("Price USD", size=10)
plt.ylabel("Country", size=10)
plt.title("All countries", size=18)
plt.tight_layout()

plt.figure(figsize=(20,12))

sns.set()
sns.barplot(
    x='price_USD', 
    y='country_name', 
    color='salmon', 
    data=bottom10,
    order=bottom10.sort_values('price_USD', ascending = False).country_name
)

# set labels
plt.xlabel("Price USD", size=10)
plt.ylabel("Country", size=10)
plt.title("All countries", size=18)
plt.tight_layout()
