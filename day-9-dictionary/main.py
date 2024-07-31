capitals = {
    "France" : "Paris",
    "Italy" : "Rome",
    "Poland" : "Warsaw"
}

travel_log = [
    {
    "country" : "France", 
    "visited_cities" : ["Paris", "Champagne", "Orleans"], 
    "total_visits" : 100
    },
    {
    "country" : "Germany", 
    "visited_cities" : ["Berlin", "Frankfurt", "Munchen"], 
    "total_visits" : 85
    },
]

travel_log += capitals
print(travel_log)