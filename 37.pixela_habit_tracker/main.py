import requests
from datetime import datetime
import os

USERNAME = "bojack"
TOKEN = os.environ["TOKEN"]
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# we already create our account so we won't need the following lines anymore
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_data ={
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=pixel_data, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

post_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?")
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
print(response.text)

change_date = "20241127"
update_pixel_endpoint = f"{post_pixel_endpoint}/{change_date}"

update_data = {
    "quantity": "2"
}
# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_pixle_endpoint = f"{post_pixel_endpoint}/{change_date}"

# response = requests.delete(url=delete_pixle_endpoint, headers=headers)
# print(response.text)