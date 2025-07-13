from tkinter import Tk, Canvas, PhotoImage, Button
from cards import Cards

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
GAME_ON = True
timer = ""

cards = Cards()
current_word = cards.get_random_word()


def countdown():
    global timer
    if len(cards.unknown_words) > 5:
        cards.save_words()
    else:
        timer = window.after(3000, flip_card)


def flip_card():
    if canvas.itemcget(lang, "text") == cards.lang1:
        canvas.itemconfig(card, image=back_image)
        canvas.itemconfig(lang, text=f"{cards.lang2}", fill="white")
        canvas.itemconfig(word, text=f"{current_word[cards.lang2]}", fill="white")
    else:
        canvas.itemconfig(card, image=front_image)
        canvas.itemconfig(lang, text=f"{cards.lang1}", fill="black")
        canvas.itemconfig(word, text=f"{current_word[cards.lang1]}", fill="black")


def wrong_answer():
    global current_word, timer
    window.after_cancel(timer)
    cards.unknown_words.append(current_word)
    current_word = cards.get_random_word()
    flip_card()
    countdown()
    print(cards.unknown_words)


def correct_answer():
    global current_word, timer
    window.after_cancel(timer)
    cards.remove_word(current_word)
    current_word = cards.get_random_word()
    flip_card()
    countdown()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
countdown()

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=front_image)
lang = canvas.create_text(400, 150, text=f"{cards.lang1}", font=(FONT, 40, "italic"), fill="black")
word = canvas.create_text(400, 300, text=f"{current_word[cards.lang1]}", font=(FONT, 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, command=wrong_answer, border=0, highlightthickness=0, bg=BACKGROUND_COLOR)
x_button.grid(row=1, column=0)

r_image = PhotoImage(file="images/right.png")
r_button = Button(image=r_image, command=correct_answer, border=0, highlightthickness=0, bg=BACKGROUND_COLOR)
r_button.grid(row=1, column=1)

window.mainloop()
