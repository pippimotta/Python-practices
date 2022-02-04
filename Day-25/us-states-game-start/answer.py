from turtle import Turtle
FONT = ('courier', 15, 'normal')
ALIGNMENT = 'center'


class Answer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_answer(self, position, state):
        self.goto(position)
        self.write(state, align=ALIGNMENT, font =FONT)