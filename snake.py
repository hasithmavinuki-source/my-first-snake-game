import turtle
class Snake :
    def __init__(self):
        self.all_body_parts = []
        self.create_snake()

    def create_snake(self) :
        n = 0
        for every_bite in range(3):
            serpent_body_parts = turtle.Turtle()
            serpent_body_parts.shape("square")
            serpent_body_parts.penup()
            serpent_body_parts.goto(n, 0)
            n -= 20
            self.all_body_parts.append(serpent_body_parts)

    def move(self):

    # move from tail to head
        for i in range( len(self.all_body_parts)-1 , 0 , -1 ):
            new_x = self.all_body_parts[i - 1].xcor()
            new_y = self.all_body_parts[i - 1].ycor()
            self.all_body_parts[i].goto(new_x, new_y)
     # move the head forward
        self.all_body_parts[0].forward(20)



    def body_growth(self) :
       serpent_body_parts = turtle.Turtle()
       serpent_body_parts.shape("square")
       serpent_body_parts.penup()
       if self.all_body_parts[0].heading() == 90 :
           x = self.all_body_parts[-1].xcor()
           y = self.all_body_parts[-1].ycor() - 20
           serpent_body_parts.setheading(90)
       elif self.all_body_parts[0].heading() == 270 :
           x = self.all_body_parts[-1].xcor()
           y = self.all_body_parts[-1].ycor() + 20
           serpent_body_parts.setheading(270)
       elif self.all_body_parts[0].heading() == 0:
           x = self.all_body_parts[-1].xcor() -20
           y = self.all_body_parts[-1].ycor()
           serpent_body_parts.setheading(0)
       else :
           x = self.all_body_parts[-1].xcor() + 20
           y = self.all_body_parts[-1].ycor()
           serpent_body_parts.setheading(180)

       serpent_body_parts.goto( x , y)
       self.all_body_parts.append(serpent_body_parts)

    def turn_right(self):
        if self.all_body_parts[0].heading() != 180:
            self.all_body_parts[0].setheading(0)

    def turn_left(self):
        if self.all_body_parts[0].heading() != 0:
            self.all_body_parts[0].setheading(180)

    def down(self):
        if self.all_body_parts[0].heading() != 90:
            self.all_body_parts[0].setheading(270)

    def up(self):
        if self.all_body_parts[0].heading() != 270:
            self.all_body_parts[0].setheading(90)








