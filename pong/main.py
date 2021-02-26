from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
from paddles import Paddle
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

ball = Ball()
ball.draw_line(screen.window_width(), screen.window_height())

scoreboard = Scoreboard()
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    if (ball.distance(right_paddle) <= 30 and ball.xcor() >= 330) or (
            ball.distance(left_paddle) <= 30 and ball.xcor() <= -330):
        ball.bounce_ball()
    elif ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.goal_player_1()
    elif ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.goal_player_2()

screen.exitonclick()
