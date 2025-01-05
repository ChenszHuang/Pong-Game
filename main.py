from turtle import Screen, Turtle
from paddle import Paddle

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

screen.onkeypress(left_pad.up, "w")
screen.onkeypress(left_pad.down, "s")
screen.onkeypress(right_pad.up, "Up")
screen.onkeypress(right_pad.down, "Down")

while True:
    screen.update()
# saya cobba tambahkan comment
# komentar kedua
screen.exitonclick()
