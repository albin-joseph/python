#In this section we mainly learn about the password manager
import os
from tkinter import *
#In thi task include following things

#------------------------ GENERATE PASSWORD --------------------#

#------------------------ SAVE PASSWORD TO FILE -----------------#

#------------------------ CREATE UI -----------------------------#

window = Tk()
window.config(width=400, height=400)

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_image = PhotoImage(file=f"{os.getcwd()}/029-day/logo.png")
canvas.create_image(100,112, image=logo_image)
canvas.grid(row=0, column=1)

window.mainloop()