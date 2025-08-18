import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("P O N G")
screen.tracer(0)


def draw_line():
    t = Turtle("square")
    t.speed("fastest")
    t.penup()
    t.goto(x=0, y=-300)
    t.setheading(90)
    t.pensize(5)
    t.color("white")
    for _ in range(15):
        t.forward(20)
        t.penup()
        t.forward(20)
        t.pendown()
    t.hideturtle()


draw_line()
my_paddle = Paddle("user")
pc_paddle = Paddle("pc")
ball = Ball()
score = Score()

screen.listen()
screen.onkey(my_paddle.up, "Up")
screen.onkey(my_paddle.down, "Down")
screen.onkey(pc_paddle.up, "w")
screen.onkey(pc_paddle.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 350:
        if ball.distance(my_paddle.xcor(), my_paddle.ycor()) < 50:
            ball.setheading(180 - ball.heading())
    if ball.xcor() < -350:
        if ball.distance(pc_paddle.xcor(), pc_paddle.ycor()) < 50:
            ball.setheading(180 - ball.heading())
    if ball.xcor() > 400:
        score.refresh_score("pc")
        ball.move_speed *= 0.9
        ball.throw_ball()
    if ball.xcor() < -400:
        score.refresh_score("player")
        ball.move_speed *= 0.9
        ball.throw_ball()

screen.exitonclick()
