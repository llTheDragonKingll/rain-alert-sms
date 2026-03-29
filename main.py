import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "YOUR_API_KEY"
account_sid = "YOUR_SID"
auth_token = "YOUR_AUTH"
FROM_NUMBER = "YOUR_TWILIO_NUMBER"
TO_NUMBER = "YOUR_PHONE_NUMBER"


weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="FROM_NUMBER",
        to="TO_NUMBER"
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's not going to rain today. No need to bring an ☔️",
        from_="FROM_NUMBER",
        to="TO_NUMBER"
    )

    print(message.status)