from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.move_speed=0.1
        self.x_move=10
        self.y_move=10
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        time.sleep(self.move_speed)
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move*=-1
        self.move_speed*=0.98
    def padbounce(self):
        self.x_move*=-1
        self.move_speed*=0.98
    def game_over(self):
         self.color("white")
         self.goto(0,0)
         self.write("GAME OVER",align="center",font=("Arial", 24, "normal"))