import math
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Nunito Sans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPETITIONS = 0
CYCLE_DONE = "✅︎"
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    title.config(text="Timer")
    check_mark.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPETITIONS
    REPETITIONS += 1

    if REPETITIONS > 8:
        return

    if REPETITIONS % 8 == 0:
        title.config(text="Break")
        countdown(LONG_BREAK_MIN * 60)
    elif REPETITIONS % 2 != 0:
        title.config(text="Work")
        countdown(WORK_MIN * 60)
    else:
        title.config(text="Break")
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = "{:02d}".format(math.floor(count / 60))
    count_sec = "{:02d}".format(count % 60)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        checks = ""
        worked_sessions = math.floor(REPETITIONS / 2)
        print(worked_sessions)
        for _ in range(worked_sessions):
            checks += CYCLE_DONE
        check_mark.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro 🍅")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title = Label(text="Timer", font=(FONT_NAME, 55, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

# Pomodoro Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="data/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_b = Button(text="START", command=start_timer, highlightthickness=0, border=0, bg=YELLOW)
start_b.grid(row=2, column=0)
reset_b = Button(text="RESET", command=reset_timer, highlightthickness=0, border=0, bg=YELLOW)
reset_b.grid(row=2, column=2)

# Check marks
check_mark = Label(text="", font=(FONT_NAME, 20), bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
