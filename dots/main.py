import colorgram
import turtle as t
import random
colors = colorgram.extract('kirby.jpeg', 30)
color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, b, g)
    color_list.append(new_color)
print(color_list)

tim = t.Turtle()
t.colormode(255)

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for i in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()
