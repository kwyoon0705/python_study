from turtle import Screen, Turtle


def move_right():
    for body in snake_body:
        body.forward(20)


def move_left():
    for body in snake_body:
        body.back(20)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake_body = []

for index in range(0, 3):
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto((20 * index - 20), 0)
    snake_body.append(snake)


screen.update()

game_is_on = True
while game_is_on:
    for body in snake_body:
        body.forward(20)


screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="a", fun=move_left)

screen.exitonclick()
