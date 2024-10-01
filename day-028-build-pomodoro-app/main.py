from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
ongoing = False
do_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global ongoing
    global reps
    ongoing = False
    window.after_cancel(do_timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    return


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global ongoing
    if ongoing:
        return
    global reps
    ongoing = True
    reps += 1
    sec = select_sec(reps)
    count_down(sec)


def select_sec(reps_num):
    if reps_num % 2 == 1:
        timer_label.config(text="Work", fg=RED)
        return WORK_MIN * 60
    elif reps_num % 2 == 0:
        if reps_num % 8 == 0:
            timer_label.config(text="Break", fg=PINK)
            return LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=GREEN)
        return SHORT_BREAK_MIN * 60


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global ongoing
    if not ongoing:
        return
    count_min, count_sec = divmod(count, 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global do_timer
        do_timer = window.after(1000, count_down, count - 1)
    else:
        ongoing = False
        if reps % 2 == 0:
            mark = ""
            for _ in range(reps // 2):
                mark += CHECK_MARK
            check_mark.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=tomato_image)
timer_text = canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

check_mark = Label(highlightthickness=0, bg=YELLOW, fg=GREEN, font="bold")
check_mark.grid(row=2, column=1)

window.mainloop()
