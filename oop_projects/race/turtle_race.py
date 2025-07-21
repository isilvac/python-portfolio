import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_pos = [-70, -40, -15, 15, 40, 70]


def set_turtles():
    for index in range(0,6):
        joe = Turtle()
        joe.color(colors[index])
        joe.shape("turtle")
        joe.speed(random.randint(0,10))
        joe.teleport(x=-230, y=y_pos[index])
        turtles.append(joe)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (choose your color)")
set_turtles()
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You win! The {user_bet} turtle won!")
            else:
                print(f"You lose! The {wining_color} turtle won")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
