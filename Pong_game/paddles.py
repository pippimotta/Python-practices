from turtle import Turtle

MOVE_DISTANCE = 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()#繼承所有Turtle的屬性以及方法
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

