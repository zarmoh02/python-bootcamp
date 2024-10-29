from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
