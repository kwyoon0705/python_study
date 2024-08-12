import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle(direction="right", color="red")
left_paddle = Paddle(direction="left", color="blue")
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 292.5 or ball.ycor() <= -292.5:
        ball.bounce_y_axis()
    if ball.distance(right_paddle) < 51.5 and ball.xcor() >= 332.5:
        ball.bounce_x_axis()
    if ball.distance(left_paddle) < 51.5 and ball.xcor() <= -332.5:
        ball.bounce_x_axis()

    if ball.xcor() > 400:
        ball.reposition()
        scoreboard.left_get_score()
    if ball.xcor() < -400:
        ball.reposition()
        scoreboard.right_get_score()

    if scoreboard.score_left == 10:
        scoreboard.goto(0, 0)
        scoreboard.write("Blue is Win.", align="center", font=("Courier", 50, "normal"))
        is_game_on = False
    if scoreboard.score_right == 10:
        scoreboard.goto(0, 0)
        scoreboard.write("Red is Win.", align="center", font=("Courier", 50, "normal"))
        is_game_on = False

screen.exitonclick()
