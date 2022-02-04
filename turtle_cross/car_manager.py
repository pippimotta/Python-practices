from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self): #利用while來生成新車，一次只需要生成一輛
        random_dice = random.randint(1, 5)#控制循環中新車生成的頻率
        if random_dice == 1:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
           
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT






