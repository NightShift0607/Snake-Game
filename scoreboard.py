from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.score_increase()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER !!! Final Score: {self.score}", align="center", font=("Courier", 18, "normal"))
    
    def score_increase(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))
        self.hideturtle()