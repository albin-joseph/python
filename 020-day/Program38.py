#In this section we are going to develop snake game
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Creating Snake body BEGIBN

starting_positions = [(0,0),(-20,0), (-40, 0)]

segments = []

for position in starting_positions:
    
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
    
#Creating Snake body END


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for segment_number in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(new_x, new_y)
        
    segments[0].forward(20)
    segments[0].left(90)