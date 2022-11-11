import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("2045.jpg", 12)
screen = Screen()
screen.colormode(255)

leonardo = Turtle()
x_cor = -300
y_cor = -300


def color(colour):
    rgb = colour.rgb
    return rgb


leonardo.penup()
leonardo.setx(x_cor)


for n in range(10):
    leonardo.sety(y_cor)
    leonardo.setx(x_cor)
    for m in range(10):
        raw_color = random.choice(colors)
        leonardo.forward(50)
        leonardo.dot(20, color(raw_color))
    y_cor += 50


screen.exitonclick()