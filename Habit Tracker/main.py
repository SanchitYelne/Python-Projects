import requests
from datetime import datetime

TOKEN = "sanchit_yelne"
USERNAME = "sanchityelne"

pixela_endpoint ="https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "Min",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(graph_response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

pixel_param = {
    "date": formatted_date,
    "quantity": input("How many minutes did you exercise today ? \n")
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_param, headers=headers)
print(pixel_response.text)

update_pixel_endpoint = f"{pixel_endpoint}/{formatted_date}"

update_pixel_param = {
    "quantity": "30"
}

# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_param, headers=headers)
# print(update_pixel_response.text)

# delete_pixel_response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)
