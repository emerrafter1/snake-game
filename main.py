from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


starting_positions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.goto(position)




screen.exitonclick()