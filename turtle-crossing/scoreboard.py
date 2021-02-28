from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.color("white")
        self.penup()
        self.goto(-100, 0)
        self.hideturtle()
        self.level = Turtle()
        self.level.hideturtle()
        self.level.penup()
        self.level.color("white")
        self.level.goto(-200, 250)
        self.level.write(f"Level: {self.level_number}", font=("Courier", 18, "normal"))

    def game_over(self):
        self.write("Game over", font=FONT)

    def level_up(self):
        self.level_number += 1
        self.level.clear()
        self.level.write(f"Level: {self.level_number}", font=("Courier", 18, "normal"))
