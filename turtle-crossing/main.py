import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from random import randint
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
scoreboard = Scoreboard()
cars = []

car_manager = CarManager()

screen.listen()
screen.onkey(player.move_turtle, "Up")

car_manager.create_cars()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_cars()
    car_manager.move_to_the_end()
    car_manager.clear_car()

    # Detect collision with cars:
    for car in car_manager.cars:
        if car.distance(player) < 20:
            print("COLLISION")
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
