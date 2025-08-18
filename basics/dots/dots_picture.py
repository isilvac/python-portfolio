from turtle import Turtle, Screen
import colorgram
import random
import turtle


def get_color(array):
    """ Given the palette taken from a picture extract colors as tuples """
    rgb_colors = []
    for items in array:
        rgb_colors.append((items.rgb.r, items.rgb.g, items.rgb.b))
    print(rgb_colors)
    return rgb_colors


def next_line():
    """ Moves one line above and continues drawing dots """
    joe.penup()
    joe.goto(x=-230, y=joe.ycor() + 50)
    joe.pendown()


colors = colorgram.extract("./data/anfield.jpg", 10)
my_color_array = get_color(colors)

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Anfield dots")

joe = Turtle()
turtle.colormode(255)
joe.hideturtle()
joe.penup()
joe.goto(x=-230, y=-270)
joe.pendown()

for _ in range(100):
    if _ % 10 == 0:
        next_line()
    joe.dot(20, random.choice(my_color_array))
    joe.penup()
    joe.forward(50)
    joe.pendown()

screen.exitonclick()
