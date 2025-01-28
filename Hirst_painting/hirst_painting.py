import turtle
from turtle import Turtle, Screen
import random
# import colorgram
# rgb_color = []

# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
color = [(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247),
         (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53),
         (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149),
         (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33),
         (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90),
         (219, 178, 182), (175, 94, 98), (179, 192, 205)]

timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
timmy.pendown()

for _ in range(1, 11):
    timmy.pendown()
    for i in range(1, 10):
        timmy.color(random.choice(color))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
    timmy.penup()
    timmy.setheading(175)
    timmy.forward(450)
    timmy.setheading(0)

screen = Screen()
screen.exitonclick()
