import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = os.environ.get(EMAIL)
MY_PASSWORD = os.environ.get(PASSWORD)

MY_LATITUDE = -9.665220
MY_LONGITUDE = -35.735710


# ISS
def get_iss_position():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data = response_iss.json()
    position = data["iss_position"]

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    coordinates = (iss_latitude, iss_longitude)
    # print(data)
    return coordinates


# Rio de Janeiro
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(f"sunrise: {sunrise_hour}\nsunset: {sunset_hour}")

while True:
    time.sleep(10)
    coordinates = get_iss_position()
    current_hour = datetime.now().hour
    # print(current_hour)
    print(f"ISS latitude:{coordinates[0]} ISS longitude:{coordinates[1]}")
    print(f"My latitude:{MY_LATITUDE} My longitude:{MY_LONGITUDE}")
    if (MY_LATITUDE - 5 <= coordinates[0] <= MY_LATITUDE + 5) and (
            MY_LONGITUDE - 5 <= coordinates[1] <= MY_LONGITUDE + 5) and (
            current_hour >= sunset_hour or current_hour <= sunrise_hour):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=os.environ.get(EMAIL_2),
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
            )
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=os.environ.get(EMAIL_3),
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
            )
        print("Look at the sky!")
    else:
        print("The ISS is quite far from Maceió.")
