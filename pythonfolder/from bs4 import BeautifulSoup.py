import pandas as pd
from bs4 import BeautifulSoup

import requests


url = "https://opencorporates.com/companies/gb/09636367"

page = requests.get(url)



soup = BeautifulSoup(page.text, "html.parser")



info = soup.find_all("dl", {'class':'attributes dl-horizontal'})



comp_info = pd.DataFrame()

cleaned_id_text = []

for i in info[0].find_all('dt'):

    cleaned_id_text.append(i.text)

    cleaned_id__attrb_text = []

    for i in info[0].find_all('dd'):

        cleaned_id__attrb_text.append(i.text)



        comp_info['Id'] = cleaned_id_text
        comp_info['Attribute'] = cleaned_id__attrb_text
        comp_info
