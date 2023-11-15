#In this section we analyse the census data
import os
import pandas

data = pandas.read_csv(f"{os.getcwd()}/025-day/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])
#Get the Grey squirels data list
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrels)

#Get diffrenet color squirels
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

gray_squirrels_count = len(gray_squirrels)
red_squirrels_count = len(red_squirrels)
black_squirrels_count = len(black_squirrels)

print(f"Number of Gray Squirrels: {gray_squirrels_count}")
print(f"Number of Red Squirrels: {red_squirrels_count}")
print(f"Number of Black Squirrels: {black_squirrels_count}")

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv(f"{os.getcwd()}/025-day/analysed_data.csv")