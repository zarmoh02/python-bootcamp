import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_parameter={
    "lat": 60.357394,
    "lon": 8.529985,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_parameter)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=account_sid,
        to=os.environ.get("PHONE_NUM"),
        body="It's going to rain today, Don't forget the ☔!",
    )

    print(message.status)