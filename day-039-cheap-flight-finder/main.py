#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
from flight_search import FlightSearch

data_manager = data_manager.DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()
for datum in sheet_data:
    iata_code = datum["iataCode"]
    if len(iata_code) == 0:
        datum["iataCode"] = flight_search.get_iata_code(datum["city"])

data_manager.set_data(sheet_data)
