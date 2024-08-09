from turtle import Turtle

ANGLES_OF_BOUNCE = [45, 135, 225, 315]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("white")
        self.penup()

    def init_move(self):
        self.setheading(ANGLES_OF_BOUNCE[0])
        self.forward(10)


