from turtle import Turtle, Screen
import random


def turtle_init():
    my_turtle.shape("turtle")
    my_turtle.penup()
    my_turtle.setx(50)
    my_turtle.pendown()


def draw_polygon(line_length, n_start, n_end, color_list):
    color_temp = ""
    for n in range(n_start, n_end + 1):
        color = random.choice(color_list)
        while color == color_temp:
            color = random.choice(color_list)
        my_turtle.color(color)
        color_temp = color
        angle = 180 - (180 * (n - 2) / n)
        for _ in range(0, n):
            my_turtle.right(angle)
            my_turtle.forward(line_length)


colors = ["red", "blue", "green", "yellow", "orange", "purple", "brown", "coral"]
my_turtle = Turtle()
turtle_init()
draw_polygon(20, 3, 30, colors)

screen = Screen()
screen.exitonclick()
