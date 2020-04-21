import requests
import pandas as pd 
import json


response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=Jestipher')
data = response.content
print(data)


response2 = requests.get('http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=1046')
data2 = response2.json()
print(data2)

item_id = data2['item']['id']
item_price = data2['item']['current']['price']
item_name = data2['item']['name']
item_description = data2['item']['description']
item_members = data2['item']['members']

df = pd.DataFrame()
name_list = [item_name]
price_list = [item_price]
id_list = [item_id]
members_list = [item_members]
df['Names'] = name_list
df['Prices'] = price_list
df['ID'] = id_list
df['members'] = members_list

df.to_csv('C:\IT3038C\FinalProject\dapitest.csv')


