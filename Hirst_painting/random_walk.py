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


angle = [90, 180, 270, 360]
timmy.pensize(10)
timmy.speed("fastest")
for _ in range(500):
    timmy.pencolor(random_colour())
    timmy.right(random.choice(angle))
    timmy.forward(30)



screen = Screen()
screen.exitonclick()
