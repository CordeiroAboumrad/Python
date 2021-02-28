from turtle import Screen, Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_head = None

    def create_snake(self):
        for x in range(0, -60, -20):
            self.add_segment(x, 0)
        self.snake_head = self.segments[0]

    def add_segment(self, x, y):
        segment = Turtle()
        segment.penup()
        segment.setpos(x, y)
        segment.color("white")
        segment.shape("square")
        self.segments.append(segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_num - 1].xcor()
            y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_position, y_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def go_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def go_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def go_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def go_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())
