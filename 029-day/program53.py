#In this section we mainly learn about the password manager
import os
from tkinter import *
#In thi task include following things

#------------------------ GENERATE PASSWORD --------------------#

#------------------------ SAVE PASSWORD TO FILE -----------------#

#------------------------ CREATE UI -----------------------------#

window = Tk()
window.config(width=400, height=400)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=f"{os.getcwd()}/029-day/logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(row=1, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.config(width=35)
email_entry.grid(row=2, column=1, columnspan=2)



password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

password_button = Button(text="Generate Password")
password_button.config(width=9)
password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add")
add_button.config(width=3)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()