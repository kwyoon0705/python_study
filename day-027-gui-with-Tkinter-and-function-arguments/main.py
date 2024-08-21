from tkinter import *

# Window
window = Tk()
window.title("My First GUI Program")
window.minsize(height=300, width=500)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am  a Label.", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New Label", padx=20, pady=20)


# Button
def button_clicked():
    my_label.config(text=f"Button clicked.")


button = Button(text="Click Me.", command=button_clicked)
button.grid(column=1, row=1)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


def print_text():
    inputted_text = input.get()
    print(inputted_text)


print_btn = Button(text="Print", command=print_text)
print_btn.grid(column=2, row=0)

# Text
text_box = Text()


window.mainloop()
