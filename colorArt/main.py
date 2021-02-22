import colorgram
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.screensize(750, 750)
timmy.speed("fastest")
timmy.hideturtle()

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

rgb_colors.pop(0)
rgb_colors.pop(1)


def position_turtle():
    timmy.penup()
    timmy.backward(50 / 2)
    timmy.backward(4 * 50)
    timmy.right(90)
    timmy.forward(50 / 2)
    timmy.forward(4 * 50)
    timmy.left(90)
    timmy.pendown()


def dots_painting():
    screen.colormode(255)
    timmy.dot(20, random.choice(rgb_colors))


# print(rgb_colors)
# print(colors)

def picasso():
    for y in range(0, 10):
        if y != 0:
            timmy.penup()
            timmy.backward(9 * 50)
            timmy.left(90)
            timmy.forward(50)
            timmy.right(90)
            timmy.pendown()

        for x in range(0, 10):
            if x != 9:
                dots_painting()
                timmy.penup()
                timmy.forward(50)
                timmy.pendown()


position_turtle()
picasso()

screen.exitonclick()
