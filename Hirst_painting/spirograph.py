import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r, g, b)
    return random_colours


timmy.speed("fastest")
for i in range(int(360 / 5)):
    timmy.color(random_colour())
    timmy.circle(100)
    timmy.right(5)


screen = Screen()
screen.exitonclick()
