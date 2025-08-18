from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.points = {"pc": 0, "player": 0}
        self.refresh_score("")

    def refresh_score(self, user):
        if user == "player":
            self.points["player"] += 1
        elif user == "pc":
            self.points["pc"] += 1
        self.clear()
        self.write(f"{self.points['pc']}  {self.points['player']}",
                   align="center", font=("Courier", 55, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 55, "bold"))
