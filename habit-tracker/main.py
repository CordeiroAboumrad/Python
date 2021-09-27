import requests
import os

pixela_endpoint = os.environ.get(PIXELA_ENDPOINT)

user_params = {
    "token": os.environ.get("TOKEN"),
    "username": os.environ.get("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response=requests.post(pixela_endpoint,json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": os.environ.get("TOKEN")
}

body_params = {
    "id": "graph01",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}

# username=os.environ.get("USERNAME")
# print(username)
# print(os.environ.get("TOKEN"))

graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

response = requests.post(graph_endpoint, json=body_params, headers=headers)
print(response.text)
