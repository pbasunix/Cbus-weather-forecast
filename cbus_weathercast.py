import requests
from bs4 import BeautifulSoup

URL = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.051030000000026&lon=-83.07007999999996#.Xc18oFFKjPY")

soup = BeautifulSoup(URL.content, 'html.parser')

seven_day_forecast = soup.find(id="seven-day-forecast-body")
#print(seven_day_forecast)

weather_objects = (seven_day_forecast.find_all(class_='tombstone-container'))

print(weather_objects)


