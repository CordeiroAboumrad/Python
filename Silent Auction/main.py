from art import logo
from clear import clear

print(logo)
print("\n\nHello!\n")


execute = 'y'
bid_dictionary = {}

while(execute == 'y'):
    name = str(input("What's your name?\n"))
    bid = float(input("What's your bid?\n"))
    
    bid_dictionary[name] = bid

    execute = str(input("Are there any more bidders (y/n)?\n"))
    clear()

biggest = 0
biggest_key = ""

for key in bid_dictionary:
    if bid_dictionary[key] > biggest:
        biggest_key = key

print(f"The winner of the silent auction is {biggest_key}, with the bid of {bid_dictionary[biggest_key]}.")
