import requests

API_KEY = ""

url_param = {"lat": 37.301655,
             "lon": 126.969913,
             "appid": API_KEY}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=url_param)
response.raise_for_status()
jsonData = response.json()
print(jsonData)
