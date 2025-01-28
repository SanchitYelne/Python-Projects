from turtle import Turtle, Screen
import random

colours = ["cyan", "blue", "green", "black", "orange", "red", "gray", "yellow"]
timmy = Turtle()
timmy.shape("turtle")

for _ in range(3, 11):
    timmy.color(random.choice(colours))
    for i in range(_):
        timmy.forward(100)
        angle = 360 / _
        timmy.right(angle)

screen = Screen()
screen.exitonclick()
