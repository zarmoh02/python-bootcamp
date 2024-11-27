import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NL_EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_HEADERS = {
    "Authorization": os.environ["SHEETY_TOKEN"]
}

exersice_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


exercise_text = input("What exercise you did today? ")
exercise_payload = {
    "query": exercise_text
}

exercise_response = requests.post(url=NL_EXERCISE_ENDPOINT, headers=exersice_headers, json=exercise_payload).json()

# print(exercise_response)

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
sheety_payload = []

for exercise in exercise_response["exercises"]:
    data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),  # Round duration to an integer
            "calories": round(exercise["nf_calories"])  # Round calories to an integer
        }
    }
    sheety_payload.append(data)

for payload in sheety_payload:

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=payload, headers=SHEETY_HEADERS)



