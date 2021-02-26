from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_cars(self):
        for x in range(0, random.randint(5, 30)):
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=0.5, stretch_len=1.5)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=random.randint(-250, 250), y=random.randint(-210, 250))
            new_car.car_speed = self.car_speed
            self.cars.append(new_car)

    def add_cars(self):
        random_chance = random.randint(1, 8)
        if random_chance > 7:
            for x in range(0, random.randint(0, 3)):
                new_car = Turtle()
                new_car.penup()
                new_car.shape("square")
                new_car.shapesize(stretch_wid=0.5, stretch_len=1.5)
                new_car.setheading(180)
                new_car.color(random.choice(COLORS))
                new_car.goto(x=300, y=random.randint(-210, 250))
                new_car.car_speed = self.car_speed
                self.cars.append(new_car)

    def move_to_the_end(self):
        for car in self.cars:
            if car.xcor() > -350:
                car.forward(self.car_speed)

    def clear_car(self):
        for car in self.cars:
            if car.xcor() >= -350:
                car.clear()

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
        print(f"Car speed: {self.car_speed}")
