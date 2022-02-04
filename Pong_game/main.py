from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score, DashLine
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor('black')
screen.setup(800, 600)

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Score((100, 220))
l_scoreboard = Score((-130, 220))
dash = DashLine()
game_is_on = True


screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(quit, 'n')
while game_is_on:
    time.sleep(ball.move_speed)  # 暫停while-loop的時間
    screen.update()  # 需要用while循環來使update每次都生效
    ball.move()  # 類比snake

    # detect if ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # 利用循環使球持續前進，僅僅是方向的改變

    # detect if ball hit the paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()



    # detect if ball out of bounds
    if ball.xcor() > 380:  # 分開寫便於計分
        ball.ball_reset()
        l_scoreboard.add_score()

    if ball.xcor() < -380:
        ball.ball_reset()
        r_scoreboard.add_score()
    # update ball
    if r_scoreboard.score == 5 or l_scoreboard.score == 5:
        ball.update()
        time.sleep(0.001)

    # decide who wins
    if r_scoreboard.score == 11 or l_scoreboard.score == 11:
        game_is_on = False
        if r_scoreboard.score > l_scoreboard.score:
            r_scoreboard.final_score('Right')
        elif r_scoreboard.score > l_scoreboard.score:
            r_scoreboard.final_score('Both winner')
        else:
            l_scoreboard.final_score('Left')

screen.exitonclick()
