import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_LOOPS = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing the street")
screen.tracer(0)
screen.listen()

t = Player()
cm = CarManager()
scoreboard = Scoreboard()
screen.onkey(t.move, "Up")

game_is_on = True
loop = 0
while game_is_on:
    if loop % CAR_LOOPS == 0:
        cm.new_car()
    cm.move(scoreboard.level)
    for car in cm.all_cars:
        if t.distance(car.xcor(), car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False
    time.sleep(0.1)
    loop += 1
    if t.is_at_the_finish_line():
        scoreboard.new_level()
        t.new_level()
    screen.update()

screen.exitonclick()
