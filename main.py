from tkinter import *


# Create miles to Km function
def distance_converter(distance):
    return round(distance * 1.609, 2)


# Setup window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


# Setup labels
equality = Label(text="is equal to")
equality.grid(column=0, row=1)
equality.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=20, pady=20)

kilometres = Label(text="Km")
kilometres.grid(column=2, row=1)
kilometres.config(padx=20, pady=20)

answer = Label(text="0")
answer.grid(column=1, row=1)
answer.config(padx=20, pady=20)


# Setup button
def button_clicked():
    miles_dist = float(user_input.get())
    km_dist = distance_converter(miles_dist)
    answer.config(text=km_dist)


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)
calculate.config(padx=10, pady=10)


# Setup entry
user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)


window.mainloop()
