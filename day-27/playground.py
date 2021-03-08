def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)
    return sum


add(1, 3, 5, 7, 9)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"The result of the calculations is {n}.")


calculate(10, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


my_car = Car(make="Nissan")
print(my_car.make, my_car.model, my_car.color)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)