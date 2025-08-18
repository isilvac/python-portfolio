import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.color("white")
        self.throw_ball()
        self.move_speed = 0.05

    def move(self):
        direction = self.heading()
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(360 - direction)
        self.forward(10)

    def throw_ball(self):
        self.home()
        self.setheading(random.randint(0, 360))
