import requests
import datetime as dt

LAT_NK = 39.036536260737826
LNG_NK = 125.73107691828159

now = dt.datetime.now()

parameters = {  # pyeongyang
    "lat": LAT_NK,
    "lng": LNG_NK,
    "tzid": "Asia/Hong_Kong",
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
