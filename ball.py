from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.step = [-1, 1]
        self.ball_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1
        if self.ball_speed - 0.002 != 0:
            self.ball_speed -= 0.002

    def respawn_ball(self):
        self.goto(0, 0)
        self.ball_speed = 0.04
        self.x_step *= random.choice(self.step)
        self.y_step *= random.choice(self.step)
