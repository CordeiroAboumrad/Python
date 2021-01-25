from menu import MENU, resources


def price(drink_preference):
    drink_price = MENU[drink_preference]["cost"]
    return drink_price


def availability(drink_preference):
    count_unavailability = 0
    for ingredient in MENU[drink_preference]["ingredients"]:
        if resources[ingredient] < MENU[drink_preference]["ingredients"][ingredient]:
            count_unavailability += 1

    if count_unavailability > 0:
        print("Not enough resources available. Sorry :(")
        return False
    else:
        return True
