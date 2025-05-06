from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            new_square.speed("slowest")
            self.snake_segments.append(new_square)

    def move(self):
        for seg in range(len(self.snake_segments)-1,  0, -1):
            new_x = self.snake_segments[seg - 1].xcor()
            new_y = self.snake_segments[seg-1].ycor()
            self.snake_segments[seg].goto(new_x, new_y)
        self.snake_segments[0].fd(MOVE_DISTANCE)



