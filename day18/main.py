from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()
screen.colormode(255)


def adjust_turtle():
    timmy.penup()
    timmy.goto(-100, 100)
    timmy.pendown()


def shape(number_of_sides):
    for x in range(number_of_sides):
        timmy.forward(100)
        timmy.right(360 / number_of_sides)


def alternate():
    timmy.penup()
    timmy.backward(500)
    timmy.pendown()
    for x in range(50):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def random_walk():
    timmy.pensize(10)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy.color(r, g, b)
    timmy.speed(100)
    direction = {
        1: timmy.forward(30),
        2: timmy.right(randint(0, 360)),
        3: timmy.left(randint(0, 360))
    }
    random_direction = randint(1, 3)
    direction.get(random_direction, "Not a valid movement")


def psychedelic_circle():
    timmy.speed(100)
    for x in range(0, 360, 5):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        timmy.color(r,g,b)
        timmy.left(5)
        timmy.circle(100)


timmy.shape("turtle")
timmy.color("red")

# adjust_turtle()

# for x in range(3, 11):
#     shape(x)
# n = 1
# while n == 1:
#     random_walk()

psychedelic_circle()

# alternate()
screen.exitonclick()
