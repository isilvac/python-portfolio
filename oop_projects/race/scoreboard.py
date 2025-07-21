from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.points = {"pc": 0, "player": 0}
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def new_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
