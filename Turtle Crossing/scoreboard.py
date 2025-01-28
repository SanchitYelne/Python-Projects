from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=260)
        self.new_level = 0

    def level(self):
        self.clear()
        self.new_level += 1
        self.write(f"Level: {self.new_level}", font=FONT)

    def game_over(self):
        self.goto(x=-50, y=0)
        self.write("GAME OVER", font=FONT)
