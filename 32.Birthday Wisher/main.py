import pandas
import datetime as dt
import random
import smtplib
from email.message import EmailMessage

MY_EMAIL = "bojack.python@gmail.com"
MY_PASSWORD = "furh ltqe zawe rbnp"

now = dt.datetime.now()
today_date = (now.month, now.day)

bday_data = pandas.read_csv("birthdays.csv")
bday_dict = {(row['month'], row['day']): row for (index, row) in bday_data.iterrows()}

if today_date in bday_dict:
    bday_person = bday_dict[today_date]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        content = letter_file.read()
        letter = content.replace("[NAME]", bday_person["name"])

    # Create the email
    msg = EmailMessage()
    msg.set_content(letter)  # Email body
    msg["Subject"] = "Happy Birthday!"  # Email subject
    msg["From"] = MY_EMAIL
    msg["To"] = bday_person["email"]

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Encrypt the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)  # Login to your email
        connection.send_message(msg)  # Send the email

# By using "python.anywhere.come" you can run your code everyday on a given time. so your code will run on the cloud and
# it'll work automatically.
