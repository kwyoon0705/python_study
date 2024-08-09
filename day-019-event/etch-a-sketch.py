from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.back(10)


def rotate_right():
    my_turtle.right(10)


def rotate_left():
    my_turtle.left(10)


def clean_draw():
    my_turtle.home()
    my_turtle.clear()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="c", fun=clean_draw)
screen.exitonclick()
