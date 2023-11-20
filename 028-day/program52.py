# In this section we are going to leran more about the GUI programs
#We are going to create a promodoro
import os
from tkinter import * 

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=f"{os.getcwd()}/028-day/tomato.png")
canvas.create_image(100,112, image=tomato_image)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start")
start_button.config(bg=YELLOW)
start_button.grid(row=2, column=0)

stop_button = Button(text="Stop")
stop_button.config(bg=YELLOW)
stop_button.grid(row=2, column=2)

window.mainloop()