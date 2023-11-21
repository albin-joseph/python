#In this section we mainly learn about the password manager
import os
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#In thi task include following things

#------------------------ GENERATE PASSWORD --------------------#

def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#------------------------ SAVE PASSWORD TO FILE -----------------#

def save_credential():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) > 0 and len(email) > 0 and len(password) > 0:
    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                            f"\nPaasword: {password}\n Is it ok to save?"
                            )
        if is_ok:
            with open(f"{os.getcwd()}/029-day/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Pasword manager", message="Please enter all the values")

#------------------------ CREATE UI -----------------------------#

window = Tk()
window.title("Passord Manager")
window.config(width=400, height=400)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=f"{os.getcwd()}/029-day/logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "albinjoseph@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.config(width=9)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save_credential)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()