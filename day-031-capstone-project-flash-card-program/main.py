from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/french_words.csv")


word_dict = word_data.to_dict(orient="records")
current_card = {}


# -------------------- FUNCTION SETUP -------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=img_card_fr)
    flip_timer = window.after(3000, func=flip_card)
    return


def is_known():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=img_card_bk)
    return


# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("FlashVoca")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
img_card_fr = PhotoImage(file="images/card_front.png")
img_card_bk = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=img_card_fr)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# -------------------- BUTTON SETUP -------------------- #
img_btn_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_btn_wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(column=0, row=1)

img_btn_right = PhotoImage(file="images/right.png")
btn_right = Button(image=img_btn_right, highlightthickness=0, command=is_known)
btn_right.grid(column=1, row=1)

next_card()

window.mainloop()
