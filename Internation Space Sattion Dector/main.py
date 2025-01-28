import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 20.593683
MY_LONG = 78.962883

responses = requests.get(url="http://api.open-notify.org/iss-now.json")
responses.raise_for_status()

data = responses.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

positions = (longitude, latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

while True:
    time.sleep(60)
    if (MY_LONG - 5) <= longitude <= (MY_LONG + 5) and (MY_LAT - 5) <= latitude <= (MY_LAT + 5):

        time_now = datetime.now().hour

        if time_now <= sunrise and time_now >= sunset:
            my_gmail = "sanchityelne06@gmail.com"
            password = "hhtf vtrf awcj nkqr"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=password)
                connection.sendmail(from_addr=my_gmail,
                                    to_addrs="sanchityelne05@gmail.com",
                                    msg="LOOK UP \n\n The ISS is above you in the sky.")


