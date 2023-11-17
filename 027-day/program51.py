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