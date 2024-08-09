from turtle import Turtle, Screen
import random


def random_walk():
    my_turtle.right(random.choice(tilt_angles))
    my_turtle.color(random_color())
    my_turtle.forward(20)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed(10)
tilt_angles = [-90, 0, 90, 180]
screen.colormode(255)
for n in range(0, 300):
    random_walk()


screen.exitonclick()


