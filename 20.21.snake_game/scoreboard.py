from turtle import Turtle

START_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(START_POSITION)
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}, Highest score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
