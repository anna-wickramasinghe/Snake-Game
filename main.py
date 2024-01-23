from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving snake
flag = True
while flag:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detecting food hts and scores up
    if snake.head.distance(food) < 15:
        food.food_refresh()
        snake.extend_snake()
        scoreboard.score_up()

    # Detecting collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with tail
    for seg in snake.vipers[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
