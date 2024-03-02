import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update()

    def write_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

    def read_high_score(self):
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())


