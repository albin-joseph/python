from tkinter import *
import os

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, columnspan=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Some question text", 
            fill=THEME_COLOR,
            font=("Ariel",20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file=f"{os.getcwd()}/034-day/quizzler/images/true.png")
        false_image = PhotoImage(file=f"{os.getcwd()}/034-day/quizzler/images/false.png")
        
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        
        self.window.mainloop()