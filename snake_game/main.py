from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True
speed = 0
while game_is_on:
    screen.update()
    time.sleep(0.2 - speed*0.01)
    snake.move()

    #detect collusion with food
    if snake.segments[0].distance(food) < 15:#用distance比较蛇头和食物之间的距离
        food.refresh()
        snake.add_body()
        scoreboard.add_score()
        if scoreboard.score % 5 == 0:
            speed += 1

    #detect collusion with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collusion with your own tail
    #if head collide with any segment
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
