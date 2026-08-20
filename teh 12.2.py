
import requests

api_key = "970e4d752ee9f562a21180a13bd70ed3"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "en"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(weather)
    print(temperature, "°C")

else:
    print("Weather information not found!")
