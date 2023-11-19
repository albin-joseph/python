# In this section we mainly focussing on creating GUI program using Tkinter
import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack()

#It hold the window on the screen
window.mainloop()

#To add unlimitted arguments to a methos let's use a parameter *args

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(5,10,15)
    