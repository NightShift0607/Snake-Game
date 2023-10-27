from turtle import Turtle
X_POSITION = 0
Y_POSITION = 0
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for i in range(3):
            self.add_block(i)
    
    def add_block(self, position):
        snake_turtle = Turtle(shape="square")
        snake_turtle.penup()
        snake_turtle.color("white")
        snake_turtle.goto(X_POSITION - position * 20 , Y_POSITION)
        self.snake.append(snake_turtle)
    
    def extend(self):
        self.add_block(len(self.snake))
    
    def move_snake(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x , y)
        self.snake[0].forward(MOVE_DIST)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)