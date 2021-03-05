numbers = [1, 2, 3]
new_numbers = [number + 1 for number in numbers]
print(new_numbers)

name = "Aboumrad"

letters_list = [letter for letter in name]
print(letters_list)

range(1, 5)
range_list = [number * 2 for number in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
