from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # Detect Collision from food
    if snake.head.distance(food) <= 15:
        food.new_position()
        snake.extend()
        scoreboard.score += 1
        scoreboard.score_increase()
    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        flag = False
        scoreboard.game_over()
    # Detect Collision with tail
    for block in snake.snake[1:]:
        if snake.head.distance(block) < 10:
            flag = False
            scoreboard.game_over()

screen.exitonclick()