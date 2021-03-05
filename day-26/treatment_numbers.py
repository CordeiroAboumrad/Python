import pandas

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

with open("file1.txt", "r") as file_1:
    chars_in_1 = file_1.readlines()
    adjusted_numbers_in_1 = [int(char) for char in chars_in_1]

with open("file2.txt", "r") as file_2:
    chars_in_2 = file_2.readlines()
    adjusted_numbers_in_2 = [int(char) for char in chars_in_2]

print(adjusted_numbers_in_1)
print(adjusted_numbers_in_2)

# numbers_in_common = [number for number in adjusted_numbers_in_1 if
#                      adjusted_numbers_in_2.__contains__(number)]

numbers_in_common = [number for number in adjusted_numbers_in_1 if
                     number in adjusted_numbers_in_2]
print(numbers_in_common)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
print(words)

result = {word: len(word) for word in words}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

fahrenheit = {day: (celsius * 9 / 5) + 32 for (day, celsius) in weather_c.items()}
print(fahrenheit)

# print(pandas.DataFrame(fahrenheit))
