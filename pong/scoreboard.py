from turtle import Turtle
import paddles
import ball
FONT = ("Arial", 30, "normal")

class Scoreboard():

    def __init__(self):
        self.score1 = Turtle()
        self.score1.penup()
        self.score1.hideturtle()
        self.score1.color("white")
        self.score1.goto(x=-200, y=250)
        self.score1.shapesize(20)
        self.score1.shapesize(20)
        self.score_player_1 = 0
        self.score1.write(f"{self.score_player_1}", font=FONT)

        self.score2 = Turtle()
        self.score2.penup()
        self.score2.hideturtle()
        self.score2.color("white")
        self.score2.goto(x=200, y=250)
        self.score_player_2 = 0
        self.score2.write(f"{self.score_player_2}", font=FONT)

    def goal_player_1(self):
        self.score_player_1 += 1
        self.score1.clear()
        self.score1.write(f"{self.score_player_1}", font=FONT)

    def goal_player_2(self):
        self.score_player_2 += 1
        self.score2.clear()
        self.score2.write(f"{self.score_player_2}", font=FONT)
