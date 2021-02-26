from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.hideturtle()

        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(x=x_axis, y=y_axis)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.showturtle()

    def go_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def go_down(self):
        if self.ycor() > -250:
            self.backward(20)
