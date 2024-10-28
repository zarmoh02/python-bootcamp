from turtle import Turtle

START_POSITION = (0, 270)
START_SCORE = 0
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(START_POSITION)
        self.score = START_SCORE
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
