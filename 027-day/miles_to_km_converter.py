import tkinter

window = tkinter.Tk()
window.title("Miles to km Converter")

miles_input = tkinter.Entry()
miles_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="miles")
miles_label.grid(row=0, column=2)

equals_label = tkinter.Label(text="is equal to")
equals_label.grid(row=1, column=0)

convertered_label = tkinter.Label(text="-")
convertered_label.grid(row=1, column=1)

km_label = tkinter.Label(text="km")
km_label.grid(row=1, column=2)

def convert_miles_to_km():
    result = float(miles_input.get()) * 1.60934
    convertered_label.config(text="{:.2f}".format(result))
    

convert_button = tkinter.Button(text="convert", command=convert_miles_to_km)
convert_button.grid(row=2, column=1)






window.mainloop()