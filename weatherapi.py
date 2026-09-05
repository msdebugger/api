import requests

city = input("Enter city name: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_data = requests.get(geo_url).json()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

weather_data = requests.get(weather_url).json()

current = weather_data["current"]

print("City:", city)
print("Temperature:",current["temperature_2m"],"oC")
print("Humidity:", current["relative_humidity_2m"],"%")
print("Wind Speed:", current["wind_speed_10m"],"km/h")

