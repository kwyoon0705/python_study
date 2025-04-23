import requests
import datetime

datetime = datetime.datetime
USER_NAME = "geonwooyun"
TOKEN = "qweradsasfzvzvbbcnvmbn"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Tracker",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

header_token = {
    "X-USER-TOKEN": TOKEN
}

graph1_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
data = {
    "date": "20250307",
    "quantity": "120"
}
# response = requests.post(url=graph1_endpoint, json=data, headers=header_token)
# print(response.text)

# response = requests.put(url=f"{graph1_endpoint}/20250307", json={"quantity": "200"}, headers=header_token)
# print(response.text)

response = requests.delete(url=f"{graph1_endpoint}/20250307", json={}, headers=header_token)
print(response.text)