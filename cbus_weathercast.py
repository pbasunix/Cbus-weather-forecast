import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.051030000000026&lon=-83.07007999999996#.Xc18oFFKjPY")

soup = BeautifulSoup(URL.content, 'html.parser')
seven_day_forecast = soup.find(id="seven-day-forecast-body")

weather_objects = (seven_day_forecast.find_all(class_='tombstone-container'))

day = [day.find(class_='period-name').get_text() for day in weather_objects]
desc = [desc.find(class_='short-desc').get_text() for desc in weather_objects]
temp = [temp.find(class_='temp').get_text() for temp in weather_objects]

weekly_cast = pd.DataFrame({
    'day': day,
    'desc': desc,
    'temp': temp,
})

print(weekly_cast)

weekly_cast.to_csv('cbus_cast.csv')
