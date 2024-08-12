from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("white")
        self.penup()
        self.move_x = 2.5
        self.move_y = 2.5
        self.move_speed = 0.01

    def move(self):
        moved_x = self.xcor() + self.move_x
        moved_y = self.ycor() + self.move_y
        self.goto(moved_x, moved_y)

    def bounce_y_axis(self):
        self.move_y *= -1
        self.move_speed *= 0.99

    def bounce_x_axis(self):
        self.move_x *= -1
        self.move_speed *= 0.99

    def reposition(self):
        self.move_speed = 0.01
        self.goto(0, 0)
        self.bounce_x_axis()
        self.move()
