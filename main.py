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
sleep_time = 0.04

screen.onkeypress(left_pad.up, "w")
screen.onkeypress(left_pad.down, "s")
screen.onkeypress(right_pad.up, "Up")
screen.onkeypress(right_pad.down, "Down")

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
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
        score.increment_left()
        score.count_score()
        ball.respawn_ball()
        sleep_time = 0.04
    elif ball.xcor() < -420:
        print("pass left")
        score.increment_right()
        ball.respawn_ball()
        sleep_time = 0.04

    if not score.check_score():
        game_on = False

screen.exitonclick()
