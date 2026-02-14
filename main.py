import turtle
import time
import snake
from apple import Apple
from score_board import Scoreboard

food = Apple()
score = Scoreboard()

nokia_screen = turtle.Screen()
nokia_screen.setup(width= 600 , height= 600)
nokia_screen.bgcolor("SpringGreen4")
nokia_screen.title("Snake Game")

nokia_screen.tracer(0)

surpent = snake.Snake()


nokia_screen.onkeypress(surpent.turn_right , "Right")
nokia_screen.onkeypress(surpent.turn_left, "Left")
nokia_screen.onkeypress(surpent.up, "Up")
nokia_screen.onkeypress(surpent.down, "Down")

nokia_screen.listen()

game_is_on = True
while game_is_on :
    surpent.move()
    time.sleep(0.1)
    nokia_screen.update()
    if surpent.all_body_parts[0].distance(food) < 25 :
        food.refresh()
        score.update_score()
        surpent.body_growth()
    x_pos = surpent.all_body_parts[0].xcor()
    y_pos = surpent.all_body_parts[0].ycor()
    if x_pos > 280 or x_pos < -280 or y_pos > 280 or y_pos < -280:
        score.game_over()
        game_is_on = False

    for  i in surpent.all_body_parts[1:] :
        if i.distance(surpent.all_body_parts[0]) < 15 :
            score.game_over()
            game_is_on = False

nokia_screen.exitonclick()
