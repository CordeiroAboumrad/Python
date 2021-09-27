import requests
import os
from twilio.rest import Client

# Coordinates for Maceió
LATITUDE = -9.665220
LONGITUDE = -35.735710
KEY = os.environ.get("KEY")

account_sid = os.environ.get("ACCOUNTSID")
auth_token = os.environ.get("AUTHTOKEN")
client = Client(account_sid, auth_token)

request = f"https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(request, params=weather_params)
response.raise_for_status()

data = response.json()
# print(data)

# for i in range(0, 13):
#     weather_id = data["hourly"][i]["weather"][0]["id"]
#     if weather_id < 700:
#         print(f"weather id: {weather_id}\n{i} hours from now.")

weather_slice = data["hourly"][:12]
is_gonna_rain = False
for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    print(condition)
    if condition < 700:
        print("Bring an umbrella.")
        is_gonna_rain = True

if is_gonna_rain:
    message = client.messages \
        .create(
        body="Bring an ☂️ , it's gonna rain.",
        from_='+19124212836',
        to='+5521975847827'
    )

    print(message.status)
