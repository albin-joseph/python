# In this section we mainly focussing on creating GUI program using Tkinter
import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
#By using place keyword used to decide the widget location.
my_label.place(x=0, y=0)

#Other than place we can use Grid to arrange items in screen.
# my_label.pack()

def button_clicked():
    my_label.config(text=input.get())
    print("button clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()

text = tkinter.Text(height=5, width=25)

text.focus()
text.pack()

#It hold the window on the screen
window.mainloop()

#To add unlimitted arguments to a methos let's use a parameter *args

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(5,10,15)
    