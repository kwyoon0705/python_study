from tkinter import *


def calculate():
    miles_num = float(miles_text.get())
    kilometers = miles_num * 1.609
    kilo_label.config(text=f"{kilometers}")


window = Tk()
window.title("Miles to Kilometers Program")
window.minsize(width=80, height=40)
window.config(padx=20, pady=20)

miles_text = Entry()
miles_text.config(width=10)
miles_text.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

desc_label = Label(text="is equal to", font=("Arial", 15))
desc_label.grid(column=0, row=1)

kilo_label = Label(text="0", font=("Arial", 15, "bold"))
kilo_label.grid(column=1, row=1)

km_label = Label(text="Km.", font=("Arial", 15))
km_label.grid(column=2, row=1)

btn_calc = Button(text="Calculate.", command=calculate)
btn_calc.grid(column=1, row=2)


window.mainloop()