import requests
import pandas as pd 
import json
import osrs-json-hiscores

# response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=Jestipher')
# data = response.content
# print(data)


# response2 = requests.get('http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=1046')
# data2 = response2.json()
# item_price = data2['item']['current']['price']
# item_name = data2['item']['name']

# print(item_price, item_name)

const hiscores = require('osrs-json-hiscores')