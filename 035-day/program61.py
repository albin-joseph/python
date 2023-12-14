import requests
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
weather_params = {
    "lat": 9.981636,
    "lon": 76.299881,
    "appid":api_key,
    "cnt": 4
}


response = requests.get(OWM_ENDPOINT,params=weather_params)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella.")