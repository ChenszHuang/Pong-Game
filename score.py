from turtle import Turtle


class Score(Turtle):
    ALIGN = "center"
    FONT = ("Arial", 40, "bold")

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(self.xcor(), 220)
        self.count_score()

    def count_score(self):
        self.clear()
        self.write(
            f"{self.left_score} | {self.right_score}",
            align=Score.ALIGN,
            font=Score.FONT,
        )
