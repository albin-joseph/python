#In this section we are going to learn about prgrams with csv data and `Pandas` library in python
import os

# with open(f"{os.getcwd()}/025-day/weather_data.csv") as weather_data_file:
#     weather_data = weather_data_file.readlines()
#     for weather in weather_data:
#         print(weather)

import csv

with open(f"{os.getcwd()}/025-day/weather_data.csv") as weather_data_file:
    data = csv.reader(weather_data_file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
            
    print(temperature)
    

import pandas

data = pandas.read_csv(f"{os.getcwd()}/025-day/weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list)/len(temp_list)
print(average_temp)

#Get column
print(data["temp"])

#Get Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


#Create Data Frame from scratch
data_dict = {
    "students":["Albin", "Anu", "Emmanuel", "Rebecca"],
    "scores": [90, 95, 100, 100]
}

data = pandas.DataFrame(data_dict)
data.to_csv(f"{os.getcwd()}/025-day/student_scores.csv")