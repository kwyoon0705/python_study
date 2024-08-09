import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a Color : ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
turtles = []
for index in range(0, 7):
    race_turtle = Turtle(shape="turtle")
    race_turtle.penup()
    race_turtle.color(colors[index])
    race_turtle.goto(-230, 150 - (50 * index))
    turtles.append(race_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost... The {winning_color} turtle is the winner!")
            break
        moving_distance = random.randint(0, 10)
        turtle.forward(moving_distance)



screen.exitonclick()
