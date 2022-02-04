from turtle import Turtle
import random


class Food(Turtle):  # inherit from Turtle class

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
