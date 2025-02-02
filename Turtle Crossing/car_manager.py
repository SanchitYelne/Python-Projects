from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            new_car.setheading(180)
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

