import requests

API_KEY = ""
APP_ID = ""
GENDER = "MALE"
WEIGHT_KG = "110"
HEIGHT_KG = "182"
AGE = "29"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_KG,
    "age": AGE
}
response = requests.post(endpoint, json=parameters, headers=headers)

result = response.json()

print(result)
