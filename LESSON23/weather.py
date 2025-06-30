from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getCurrWeather(city='oyo'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    print('\n***** Get Current Weather Condition *****\n')

    city = input('Please enter a city name\n\n')

    # Checks for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'oyo'

    weather_data = getCurrWeather(city)

    print('\n')
    pprint(weather_data)