from menu import MENU, resources
from sum import count
from price_and_availability import price, availability

# TODO: 1. Print report of all coffee machine resources

# TODO: 2. Check resources sufficient to make drink order.

# TODO: 3. If available, ask for the user to input money. If not, tell the user that the drink is not available

# TODO: 4. Count the money and see if it is equal or bigger than the amount requested

# TODO: 5. If it is bigger, give the tip. If equal, just prepare the drink. Else, refund and tell the customer to give more money

successful = True

while successful:
    drink_preference = input("Hello. What would you like? (espresso/latte/cappuccino): ")

    if drink_preference == "resources":
        print(resources)
    else:
        drink_price = price(drink_preference)

        available = availability(drink_preference)

        if available:
            successful = count(drink_preference, drink_price)