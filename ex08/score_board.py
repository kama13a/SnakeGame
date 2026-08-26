from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24 , 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.score_change()

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def score_change(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()







