import requests
import json 

print('Please enter your zip code:   ')
zip = input()


r = requests.get('https://api.openweathermap.org/data/2.5/weather?weather?zip=%s,us&appid=063bc2c93fab95747140072e916f07b0')
#print(type(r.content))
data = r.json()
#print(type(data))
print(data['weather'][0]['description'])