from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CREATING_FREQUENCY = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_frequency = CAR_CREATING_FREQUENCY

    def create_car(self):
        random_chance = random.randint(1, self.car_frequency)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(random.randint(270, 290), random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.car_frequency -= 1

