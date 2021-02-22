from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

winner = False

timmy = Turtle(shape="turtle")
timmy.color("red")
timmy.penup()
timmy.goto(x=-230, y=-100)

tommy = Turtle(shape="turtle")
tommy.color("orange")
tommy.penup()
tommy.goto(x=-230, y=-70)

tammy = Turtle(shape="turtle")
tammy.color("yellow")
tammy.penup()
tammy.goto(x=-230, y=-40)

chummy = Turtle(shape="turtle")
chummy.color("green")
chummy.penup()
chummy.goto(x=-230, y=-10)

blummy = Turtle(shape="turtle")
blummy.color("blue")
blummy.penup()
blummy.goto(x=-230, y=20)

purry = Turtle(shape="turtle")
purry.color("purple")
purry.penup()
purry.goto(x=-230, y=50)

turtles = {
    1: timmy,
    2: tommy,
    3: tammy,
    4: chummy,
    5: blummy,
    6: purry
}

guess = screen.numinput(title="Make your bet",
                        prompt="Which turtle do you think will win the race (type number)?\n1 - red\n2 - orange\n3 - "
                               "yellow\n4 - green\n5 - blue\n6 - purple\n")


while not winner:
    random = randint(1, 6)
    turtles[random].forward(10)
    if turtles[random].xcor() >= 250:
        print(f"{turtles[random].fillcolor()} turtle wins!")
        if random == guess:
            print("Congratulations, you've won!")
        else:
            print("Sorry, you lost.")
        winner = True

screen.exitonclick()
