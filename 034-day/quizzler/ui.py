from tkinter import *
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, columnspan=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some question text", 
            fill=THEME_COLOR,
            font=("Ariel",20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file=f"{os.getcwd()}/034-day/quizzler/images/true.png")
        false_image = PhotoImage(file=f"{os.getcwd()}/034-day/quizzler/images/false.png")
        
        self.true_button = Button(image=true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command= self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
       self.canvas.config(bg="white")
       self.score_label.config(text=f"Score: {self.quiz.score}")
       if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
       else:
           self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz") 
           self.true_button.config(state="disabled")
           self.false_button.config(state="disabled")

       
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        