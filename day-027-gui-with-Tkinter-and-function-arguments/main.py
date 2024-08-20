import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(height=300, width=500)
my_label = tkinter.Label(text="I am  a Label.", font=("Arial", 24, "bold"))
my_label.pack()



window.mainloop()
