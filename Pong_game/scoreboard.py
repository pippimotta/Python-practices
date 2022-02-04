from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(position)
        self.score = 0
        self.show_score()

    def show_score(self):
        self.write(f'{self.score}', font=("Comic Sans", 60, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def final_score(self,winner):
        self.goto(0,0)
        self.write(f'{winner} player wins by {self.score}', align='center', font=("Comic Sans", 20, "normal"))


class DashLine(Turtle):
    def __init__(self):
        super().__init__()

        self.setposition(0, 300)
        self.color('white')
        self.setheading(270)
        self.pensize(2)
        for _ in range(15): #dash_line code:先畫 再penup 再畫 再pendown
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()


