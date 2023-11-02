from turtle import Turtle
with open("data.txt") as file:
    highscore = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(highscore)
        self.color("white")
        self.penup()
        self.score_increase()
    
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_increase()
    
    
    def score_increase(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 18, "normal"))
        self.hideturtle()