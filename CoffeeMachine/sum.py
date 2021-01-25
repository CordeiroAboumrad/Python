from menu import MENU, resources


def count(drink_preference, drink_price):
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))

    total_input = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    exchange = total_input - drink_price

    if total_input < drink_price:
        print("Sorry, that's not enough money. Money refunded.\n")
        try_again = input("Do you wish to try again? (y/n)")
        if try_again == "y":
            return True
        else:
            return False
    else:
        for ingredient in resources:
            resources[ingredient] = resources[ingredient] - MENU[drink_preference]["ingredients"][ingredient]
        print(f"Total exchange: {exchange}")
        print(f"Here's your {drink_preference} ☕️ Enjoy!")
        return True
