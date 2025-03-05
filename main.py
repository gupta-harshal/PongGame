from turtle import Turtle,Screen
from Player_1 import Player
from scoreboard import Scoreboard
from ball import Ball
import time
score=Scoreboard()
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
right_paddle=Player((350,0))
left_paddle=Player((-350,0))
ball=Ball()
screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")
game_is_on=True

while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.xcor()>400 or ball.xcor()<-400:
        game_is_on=False
        ball.game_over()
    if ball.distance(right_paddle)<40 and ball.xcor()<336:
        ball.padbounce()
        score.r_point()
        score.update_score()
    if ball.distance(left_paddle)<40  and ball.xcor()>-336:
         ball.padbounce()
         score.l_point()
         score.update_score()
    
screen.exitonclick() 