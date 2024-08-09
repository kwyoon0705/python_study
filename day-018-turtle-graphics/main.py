# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_spot_painting.png", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
import random
from turtle import Turtle, Screen
extracted_colors = [(203, 34, 65), (69, 115, 151), (228, 162, 194), (150, 161, 166), (240, 235, 47),
                    (135, 205, 186), (146, 189, 70), (240, 99, 53), (33, 163, 165), (38, 161, 70), (34, 30, 31),
                    (75, 65, 40), (247, 232, 240), (237, 248, 243), (211, 219, 223), (200, 10, 54), (40, 34, 12),
                    (220, 138, 158), (181, 97, 114), (0, 155, 83), (128, 189, 38), (219, 0, 0), (111, 106, 88),
                    (157, 210, 178), (242, 173, 155)]

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random.choice(extracted_colors))
    if dot_count == number_of_dots:
        my_turtle.hideturtle()
        break
    my_turtle.forward(50)
    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        if (dot_count / 10) % 2 != 0:
            my_turtle.setheading(180)
        else:
            my_turtle.setheading(360)
        my_turtle.forward(50)













screen.exitonclick()


