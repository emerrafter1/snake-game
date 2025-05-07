from tokenize import String
from turtle import Turtle
with open("score_data.txt") as file:
    high_score = int(file.read())




ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score_data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



