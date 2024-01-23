from turtle import Turtle

MOVE_DISTANCE = 20
VIPER_LENGTH = [(0,0), (-20,0), (-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.vipers = []
        self.create_snake()
        self.head = self.vipers[0]

    # creating the snake's body
    def create_snake(self):

        for i in VIPER_LENGTH:
            self.add_segment(i)

    def add_segment(self, position):
        new_viper = Turtle(shape="square")
        new_viper.color("white")
        new_viper.penup()
        new_viper.goto(position)
        self.vipers.append(new_viper)

    def extend_snake(self):
        self.add_segment(self.vipers[-1].position())

    def reset_snake(self):
        for seg in self.vipers:
            seg.goto(1000,1000)
        self.vipers.clear()
        self.create_snake()
        self.head = self.vipers[0]

    def move(self):
        for viper in range(len(self.vipers) - 1, 0, -1):
            new_x = self.vipers[viper - 1].xcor()
            new_y = self.vipers[viper - 1].ycor()
            self.vipers[viper].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
