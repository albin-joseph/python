import requests
import datetime

USERNAME = "albin123"
TOKEN = "huywjsndks7jsbd8837jkd",
GRAPH_ID = "graph1"

pixela_api_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_api_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# post_activity_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(post_activity_response.text)

activity_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

activity_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.21",
}

activity_response = requests.post(url=activity_endpoint, json=activity_data, headers=headers)
print(activity_response.text)