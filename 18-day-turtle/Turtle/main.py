import turtle
from turtle import Turtle, Screen
import random

javad = Turtle()
javad.shape("turtle")
javad.color("DarkGreen")
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SeaGreen",
#           "SlateGray"]

"""to change the name of anything we've named, right click-> refactor, and then change the name"""
# for i in range(4):
#     """draws a square"""
#     javad.forward(100)
#     javad.right(90)

# for i in range(15):
#     """draws a dash line"""
#     javad.forward(10)
#     javad.penup()
#     javad.forward(10)
#     javad.pendown()

# num_side = 3
# for n in range(8):
#     for i in range(num_side):
#         angle = 360 / num_side
#         javad.forward(100)
#         javad.right(angle)
#     num_side += 1
#     javad.pencolor(random.choice(colors))

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# angles: list[int] = [0, 90, 180, 270]
# javad.pensize(8)
# javad.speed(0)
# while True:
#     javad.pencolor(random_color())
#     javad.right(random.choice(angles))
#     javad.forward(20)

javad.speed(0)


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        javad.pencolor(random_color())
        javad.circle(100)
        javad.left(gap_size)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
