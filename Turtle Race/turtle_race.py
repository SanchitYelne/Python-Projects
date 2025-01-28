from turtle import Turtle, Screen
import random

# tim = Turtle()
# tom = Turtle()
# mon = Turtle()
# san = Turtle()
# nom = Turtle()
# yom = Turtle()

# tim.penup()
# tom.penup()
# mon.penup()
# san.penup()
# nom.penup()
# yom.penup()
#
# tim.color("red")
# tom.color("blue")
# mon.color("green")
# san.color("yellow")
# nom.color("orange")
# yom.color("violet")
#
# tim.shape("turtle")
# tom.shape("turtle")
# mon.shape("turtle")
# san.shape("turtle")
# nom.shape("turtle")
# yom.shape("turtle")
#
# tim.goto(x=-220, y=-112)
# tom.goto(x=-220, y=-56)
# mon.goto(x=-220, y=0)
# san.goto(x=-220, y=56)
# nom.goto(x=-220, y=112)
# yom.goto(x=-220, y=168)

race_is_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose the color: ")

color = ["red", "blue", "orange", "yellow", "purple", "green"]
y_coordinate = [-112, -56, 0, 56, 112, 168]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-220, y=y_coordinate[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:

        if turtle.xcor() > 230:
            race_is_on = False
            if user_bet == turtle.pencolor():
                print(f"You Won! Winning turtle is '{turtle.pencolor()}'.")
            else:
                print(f"You Lost! Winning turtle is '{turtle.pencolor()}'")

        turtle.forward(random.randint(0, 10))


screen.exitonclick()
