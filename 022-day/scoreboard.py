from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"LScore:{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(f"RScore:{self.r_score}", align=ALIGNMENT, font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    