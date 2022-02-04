from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Comic Sans', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}  High score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.show_score()

# compare current score and high score, if True ,replace high score
    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.show_score()


    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write('Game Over.',align=ALIGNMENT, font=('Comic Sans', 20, 'normal'))

