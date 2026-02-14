from turtle import Turtle
import random
class Apple(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        # self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)




