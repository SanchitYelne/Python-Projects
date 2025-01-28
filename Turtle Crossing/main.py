import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
score.level()

player = Player()
screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    car.create_car()
    car.move()
    if player.is_at_finish_line():
        score.level()
        player.go_to_start()
        car.level_up()
        car.create_car()
    time.sleep(0.1)
    screen.update()

    for cars in car.all_car:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
