from turtle import Turtle, Screen
import random


my_turtle = Turtle()
screen = Screen()
screen.colormode(255)
my_turtle.pensize(2)
my_turtle.speed(20)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


def draw_spirograph(angle_gap, radius):
    rotation_count = int(360 / angle_gap)
    for n in range(0, rotation_count):
        my_turtle.left(angle_gap)
        my_turtle.color(random_color())
        my_turtle.circle(radius)


draw_spirograph(5, 25)
screen.exitonclick()
