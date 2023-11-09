from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.write()