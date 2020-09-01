import requests


def weather(city_name):
    city = city_name
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
    weather_data = requests.get(url).json()
    weather_main = weather_data['main']
    return weather_main


def celsius_f(faren):
    c = (int(faren) - 32) * (5/9)
    return int(c)

def celsius_k(kelvin):
    c = int(kelvin) - 273.15
    return int(c)
