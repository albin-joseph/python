from tkinter import *
import pandas
import os
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv(f"{os.getcwd()}/031-day/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
#flip_timer

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    pass

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file=f"{os.getcwd()}/031-day/images/card_front.png")
card_back_img = PhotoImage(file=f"{os.getcwd()}/031-day/images/card_back.png")

card_background = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=f"{os.getcwd()}/031-day/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=f"{os.getcwd()}/031-day/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()