# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#
# print(data)


# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

# Alternative way
average_pandas_mean = data["temp"].mean()
print(average_pandas_mean)

# Getting the maximum value
maximum_value_pandas = data["temp"].max()
print(maximum_value_pandas)

print(data[data.temp == maximum_value_pandas])

# Getting Monday's temperature and converting it to Fahrenheits
monday = data[data.day == "Monday"]
temp_fahrenheit = monday["temp"] * 9 / 5 + 32
print(temp_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
