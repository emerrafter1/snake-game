from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)


snake = []
game_over = False
starting_positions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(position)
    new_square.speed("slowest")
    snake.append(new_square)

screen.update()


while game_over == False:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(snake)-1,  0, -1):
        new_x = snake[seg - 1].xcor()
        new_y = snake[seg-1].ycor()
        snake[seg].goto(new_x, new_y)
    snake[0].fd(20)




screen.exitonclick()