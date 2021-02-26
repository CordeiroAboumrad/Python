from turtle import Turtle
from paddles import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.setpos(0, 0)
        self.color("white")
        self.direction_x = 10
        self.direction_y = 10

    def draw_line(self, width, height):
        # Create middle line for the screen
        tim = Turtle()

        tim.penup()
        tim.setpos(x=0, y=-300)
        tim.setheading(90)
        tim.hideturtle()
        tim.pencolor("white")
        tim.pensize(5)
        tim.pendown()

        while tim.ycor() < 300:
            tim.forward(20)
            tim.penup()
            tim.forward(20)
            tim.pendown()

    def move_ball(self):

        new_x = self.xcor()
        new_y = self.ycor()

        if self.ycor() >= 290:
            self.direction_y = self.direction_y - 20
            self.goto(new_x + self.direction_x, new_y + self.direction_y)

        elif self.ycor() <= -290:
            self.direction_y = self.direction_y + 20
            self.goto(new_x + self.direction_x, new_y + self.direction_y)
        else:
            self.goto(new_x + self.direction_x, new_y + self.direction_y)

    def bounce_ball(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.direction_x *= -1
        self.goto(new_x + self.direction_x, new_y + self.direction_y)
        print("Ball hit the wall")

    def reset_ball(self):
        self.direction_x *= -1
        self.direction_y *= -1
        self.goto(0, 0)