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

    def increment_left(self):
        self.left_score += 1
        self.count_score()

    def increment_right(self):
        self.right_score += 1
        self.count_score()

    def check_score(self):
        if self.left_score == 10 or self.right_score == 10:
            self.goto(0, 0)
            self.write("Game Over", align=Score.ALIGN, font=Score.FONT)
            return False
        return True
