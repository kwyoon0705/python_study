import os
import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._api_token = self._get_new_token()
        self.base_url = "https://test.api.amadeus.com/v1"

    def _get_new_token(self):
        endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {"grant_type": "client_credentials",
                "client_id": self._api_key,
                "client_secret": self._api_secret}

        response = requests.post(url=endpoint, headers=header, data=body)
        return response.json()["access_token"]

    def get_iata_code(self, city_name):
        location_url = "/reference-data/locations"
        header = {
            "accept": "application/vnd.amadeus+json",
            "Authorization": f"Bearer {self._api_token}"
        }
        parameter = {
            "subType": "CITY",
            "keyword": city_name
        }
        url = self.base_url + location_url
        response = requests.get(url, params=parameter, headers=header).json()
        data = response["data"]
        for item in data:
            if item["address"]["cityName"] == city_name.upper():
                return item["address"]["cityCode"]



