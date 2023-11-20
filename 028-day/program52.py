# In this section we are going to leran more about the GUI programs
#We are going to create a promodoro
import os
from tkinter import * 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps%8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60) 
    count_sec = count%60
    if count_sec < 10:
        #Here we use the dynamic type. Python allow to set a varaible/ assign a variable different type
        #So we can say python is strongly a `Dynamic Type` language
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer =  window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_seessions = math.floor(reps/2)
        for _ in range(work_seessions):
            marks += "✓"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=f"{os.getcwd()}/028-day/tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

stop_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
stop_button.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW )
check_mark.grid(row=2, column=1)

window.mainloop()