from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        random_X = randint(-280, 280)
        random_Y = randint(-280, 280)
        self.goto(random_X, random_Y)