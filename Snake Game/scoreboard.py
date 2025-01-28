from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = 0
        with open("data.txt", "r") as data:
            self.high_score = data.read()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)

    def reset(self):
        self.new_score = 0
        self.high_score = 0
        if self.new_score > self.high_score:
            self.high_score = self.new_score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score()

    def increase_score(self):
        self.clear()
        self.new_score += 1
        self.score()

    def score(self):
        self.clear()
        self.write(f"Score : {self.new_score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)


