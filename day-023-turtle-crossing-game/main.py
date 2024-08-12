import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.finish_line():
        player.move_to_start()
        car_manager.level_up()
        score_board.increase_level()


screen.exitonclick()
