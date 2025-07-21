import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def new_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.teleport(x=275, y=random.randint(-260, 260))
        car.setheading(180)
        self.all_cars.append(car)

    def move(self, level):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + level)
