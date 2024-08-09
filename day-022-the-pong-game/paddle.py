from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
RIGHT_PADDLE_LOCATION = (350, 0)
LEFT_PADDLE_LOCATION = (-350, 0)


class Paddle(Turtle):

    def __init__(self, direction, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if direction == "right":
            self.goto(RIGHT_PADDLE_LOCATION)
        if direction == "left":
            self.goto(LEFT_PADDLE_LOCATION)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
