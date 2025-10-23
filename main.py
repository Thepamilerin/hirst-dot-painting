# import colorgram
# colors = colorgram.extract('image.jpg', 45)
#
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))
# print(rgb_list)


color_list = [(249, 248, 248), (232, 241, 239), (1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7), (70, 72, 44), (186, 190, 199), (91, 48, 43), (128, 223, 230)]

from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = Screen()
screen.exitonclick()