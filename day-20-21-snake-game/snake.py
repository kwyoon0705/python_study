from turtle import Turtle

GENERATE_SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.prev_direction = "right"
        self.body_segments = []
        self.create_snake()

    def create_snake(self):
        for coordinate in GENERATE_SNAKE_POSITION:
            body_segment = Turtle()
            body_segment.shape("square")
            body_segment.color("white")
            body_segment.penup()
            body_segment.goto(coordinate)
            self.body_segments.append(body_segment)

    def move(self, direction):
        self.prev_direction = direction
        for seg_num in range(len(self.body_segments) - 1, 0, -1):
            prev_seg_x = self.body_segments[seg_num - 1].xcor()
            prev_seg_y = self.body_segments[seg_num - 1].ycor()
            self.body_segments[seg_num].goto(prev_seg_x, prev_seg_y)
        self.body_segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.prev_direction != "down":
            self.body_segments[0].setheading(90)
            self.move("up")

    def move_down(self):
        if self.prev_direction != "up":
            self.body_segments[0].setheading(270)
            self.move("down")

    def move_left(self):
        if self.prev_direction != "right":
            self.body_segments[0].setheading(180)
            self.move("left")

    def move_right(self):
        if self.prev_direction != "left":
            self.body_segments[0].setheading(0)
            self.move("right")
