from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed += 0.9
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        