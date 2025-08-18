from turtle import Turtle

PC_POS = (-360, 20)
PLAYER_POS = (360, 20)
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        if player == "user":
            self.owner = "player"
            self.goto(PLAYER_POS)
        else:
            self.owner = "machine"
            self.goto(PC_POS)
        self.color("white")
        self.speed("fast")

    def up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)