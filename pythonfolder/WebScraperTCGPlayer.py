import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://shop.tcgplayer.com/magic/ravnica-allegiance/smothering-tithe?xid=i5486525e27004ca39449bba938fc87c1").content
soup = BeautifulSoup(data, 'html.parser')

span = soup.find("h1",{"class":"product-details__name"})
title = span.text
span = soup.find("div",{"class":"product-details__set"})
productSet = span.text
span = soup.find("dd", {"class":'product-description__value'})
productDescription = span.text

print("Item name %s from %s, has a rarity of %s of the set" % (title, productSet, productDescription))


