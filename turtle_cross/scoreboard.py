from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.score = 1
        self.penup()
        self.goto(-250,270)
        self.show_score()

    def show_score(self):
        self.write(f'Level: {self.score}', align='left', font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.write('Game Over ><', align='center', font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.show_score()

