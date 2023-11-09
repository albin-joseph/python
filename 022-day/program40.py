#Create classic PONG Game
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect the collision with wall and bounce
# 6. Detect collision with passdle
# 7. Detect when paddle misses
# 8. Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    # Detecting collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        #needs to bounce
        ball.bounce_y()
    # Detection collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect r_paddle misses ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    
    # Detect l_paddle misses ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        
    


screen.exitonclick()