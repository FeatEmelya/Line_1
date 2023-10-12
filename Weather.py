import datetime
import requests

# Получение местоположения пользователя

def get_location():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data['city'], data['country']

city, country = get_location()

# Получение текущей даты и времени

current_datetime = datetime.datetime.now()

# Получение погоды по местоположению пользователя

def get_weather(city):
    api_key = '5a030a4f57msh162c56be0644328p10fd5ejsne068ac57c24d'  # Замените на ваш собственный ключ API
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    temperature = int(data['main']['temp'] - 273.15) # Преобразование температуры в градусы Цельсия
    weather_description = data['weather'][0]['description']
    return temperature, weather_description

temperature, weather_description = get_weather(city)

# Вывод на главный экран MacBook

widget_text = f"Новости с полей {city}, {country}.\n"
widget_text += f"Ты посмотрел сюда в {current_datetime}.\n"
widget_text += f"Захочешь прогуляться, учти что на улице {temperature}°C with {weather_description}."

print(widget_text)