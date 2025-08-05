import requests
from pprint import pprint


class DataManager:

    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.endpoint = "https://api.sheety.co/42c570ad7714dc30828a302d56d736ee/studyFlightDeals/prices"
        self.response = requests.get(self.endpoint)
        self.result = self.response.json()

    def get_data(self):
        return self.result["prices"]

    def set_data(self, sheet_data):
        for item in sheet_data:
            body = {
                "price": {
                    # "city": item["city"],
                    "iataCode": item["iataCode"],
                    # "lowestPrice": item["lowestPrice"]
                    "id": item["id"]
                }
            }
            requests.put(url=f"{self.endpoint}/{item["id"]}", data=body)
