import json
import tkinter
import requests

API_KEY = "c8bd17b214573ae71418943906492149"

# response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid='c8bd17b214573ae71418943906492149&units=metric')

response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Amsterdam&appid=c8bd17b214573ae71418943906492149')
print(response)

data = response.json()

print(data)



# data['current']['temp']
# data['current']['humidity']


