import time
from snake import Snake
from turtle import Screen

from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor() < -270 or snake.head.xcor() > 270 or snake.head.ycor() < -270 or snake.head.ycor() > 270:
        score.reset()
        snake.reset()
    for segment in snake.body[1:]:
        if segment.distance(snake.head) < 15:
            score.reset()
            snake.reset()

screen.exitonclick()
