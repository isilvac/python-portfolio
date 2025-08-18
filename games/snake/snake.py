from turtle import Turtle

INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for pos in INITIAL_POS:
            self.add_body(pos)

    def add_body(self, pos):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(pos)
        self.body.append(t)

    def extend(self):
        self.add_body(self.body[-1].position())

    def move(self):
        for seg_pos in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_pos - 1].xcor()
            new_y = self.body[seg_pos - 1].ycor()
            self.body[seg_pos].goto(new_x, new_y)
        self.body[0].forward(STEPS)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for item in self.body:
            item.goto(800, 800)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]