from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} Highh Score:{self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    
    #def game_over(self):
       # self.goto(0,0)
        #self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)