import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

    if snake.head.distance(food) <= 15:
        food.relocate()
        scoreboard.increase_score()
        snake.increase_snake_body()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        #game_is_on = False
    for body_segment in snake.body_segments[1:]:
        if snake.head.distance(body_segment) < 10:
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            #game_is_on = False


screen.exitonclick()
