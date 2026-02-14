ALINGMENT = "center"
FONT = ("Times New Roman", 16, "normal")

from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def update_score(self) :
        self.clear()
        self.score += 1
        self.goto(0,250)
        self.write(arg=f"SCORE = {self.score}", move = False, align= ALINGMENT,font = FONT )



    def game_over(self) :
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALINGMENT, font=FONT)

