from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_over = False


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



screen.update()



while game_over == False:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect snake has ate food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()




screen.exitonclick()