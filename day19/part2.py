from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def up_move():
    tim.setheading(tim.heading() + 10)


def down_move():
    tim.setheading(tim.heading() - 10)


def right_move():
    tim.forward(10)


def left_move():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="Up", fun=up_move)
screen.onkey(key="Down", fun=down_move)
screen.onkey(key="Right", fun=right_move)
screen.onkey(key="Left", fun=left_move)
screen.onkey(key="space", fun=clear)

screen.exitonclick()
