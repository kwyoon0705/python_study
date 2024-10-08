# with open("weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
# print(data)

# import csv
#
# temperatures = []
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         temp_data = row[1]
#         if temp_data != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# temp_avg = data["temp"].mean()
# temp_max = data["temp"].max()
# print(temp_avg)
# print(temp_max)
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp[0])
# print(monday_temp)
# monday_temp_fa = monday_temp * 9 / 5 + 32
# print(monday_temp_fa)

data_dict = {
    "students": ["Amy", "Angela", "James", "Nakamura", "Kim"],
    "scores": [85, 76, 90, 96, 100]
}

data_created = pandas.DataFrame(data_dict)
print(data_created)
data_created.to_csv("new_data.csv")
