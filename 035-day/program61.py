import requests
import os
from twilio.rest import Client
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
account_sid = ''
auth_token = ''



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
    if int(condition_code) < 900:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's raining don't forget to bring umbrella",
                     from_='+18587629567',
                     to='+919744466509'
                 )
    print(message.sid, message.status)