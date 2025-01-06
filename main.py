from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

LEFT_POS = (-350, 0)
RIGHT_POS = (350, 0)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

left_pad = Paddle(LEFT_POS)
right_pad = Paddle(RIGHT_POS)

ball = Ball()
score = Score()

screen.onkeypress(left_pad.up, "w")
screen.onkeypress(left_pad.down, "s")
screen.onkeypress(right_pad.up, "Up")
screen.onkeypress(right_pad.down, "Down")

while True:
    time.sleep(0.04)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()
    if (
        ball.xcor() == 340
        and ball.distance(right_pad) < 55
        or ball.xcor() == -340
        and ball.distance(left_pad) < 55
    ):
        ball.bounce_x()
    elif ball.xcor() > 420:
        print("pass right")
        score.left_score += 1
        score.count_score()
        break
    elif ball.xcor() < -420:
        print("pass left")
        score.right_score += 1
        score.count_score()
        break
screen.exitonclick()
