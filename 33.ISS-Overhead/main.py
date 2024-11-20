import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import time

MY_EMAIL = "bojack.python@gmail.com"
MY_PASSWORD = "furh ltqe zawe rbnp"
MY_LAT = 35.776739
MY_LONG = 51.421910


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "time_format": 24,
    }

    response = requests.get("https://api.sunrisesunset.io/json/", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])
    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        # Create the email
        msg = EmailMessage()
        msg.set_content(
            "ISS is right above you,\nif the air is clean enough you can spot it.\n so look up!")  # Email body
        msg["Subject"] = "Look Up!"  # Email subject
        msg["From"] = MY_EMAIL
        msg["To"] = "zahra.mohmadi02@gmail.com"

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Encrypt the connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)  # Login to your email
            connection.send_message(msg)  # Send the email
