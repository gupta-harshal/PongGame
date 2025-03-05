from turtle import Turtle,Screen
screen=Screen()
list=[]
x_pos=350
Screen().tracer(0)
position=[(x_pos,0),(x_pos,20),(x_pos,40),(x_pos,60),(x_pos,80)]
class Player(Turtle):
    def __init__(self,position):
         super().__init__()
         self.shape("square")
         self.color("white")
         self.shapesize(stretch_wid=3,stretch_len=1)
         self.penup()
         self.goto(position)
    def go_up(self):
         new_y=self.ycor() +20
         self.goto(self.xcor(),new_y)
    def go_down(self):
         new_y=self.ycor() -20
         self.goto(self.xcor(),new_y)