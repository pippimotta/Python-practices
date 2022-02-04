import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
user_choice = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
not_over = True
turtles = []
for _ in range(len(colors)):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.color(colors[_])
    turtle.goto(x=-230, y=-120 + _ * 40)
    turtles.append(turtle)

while not_over:
    for turtle in turtles:
        speed = random.randint(1, 10)
        turtle.forward(speed)
        if turtle.xcor() > 220:#注意是> 不是=
            not_over = False
            winner = turtle.color()[0]
            if winner == user_choice:
                print('You win! You are the king of turtles 🐢.')
            else:
                print(f'You lose. The winner is {winner}.')

screen.exitonclick()
