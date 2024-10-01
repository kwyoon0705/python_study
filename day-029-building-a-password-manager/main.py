import tkinter.messagebox
from tkinter import *
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    pwd_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    pwd_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]
    password_list = pwd_letters + pwd_symbols + pwd_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_url = website_entry.get()
    email_address = email_entry.get()
    pwd_info = password_entry.get()
    if website_url == "" or email_address == "" or pwd_info == "":
        tkinter.messagebox.showwarning(title="No Info", message="You should fill all of entries.")
        return
    is_save = tkinter.messagebox.askokcancel(title=website_url, message="Do you want save it?")
    if is_save:
        with open("dummy_password.txt", "a") as data:
            data.write(f"{website_url} : {email_address} :: {pwd_info}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", width=20)
website_label.grid(row=1, column=0)
email_label = Label(text="Email: ", width=20)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", width=20)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "passwordMaker@password.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_pwd_btn = Button(text="Generate Password", width=20, command=generate_password)
generate_pwd_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=10, command=save_password)
add_btn.grid(row=4, column=1)

window.mainloop()
