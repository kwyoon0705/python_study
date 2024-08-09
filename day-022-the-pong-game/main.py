import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle(direction="right", color="red")
left_paddle = Paddle(direction="left", color="blue")
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

is_game_on = True
angle_of_ball = 45
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.init_move()


screen.exitonclick()
