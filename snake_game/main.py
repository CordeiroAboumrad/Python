from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.create_snake()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.snake_head.distance(food) < 19:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # Detect collision with wall
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
