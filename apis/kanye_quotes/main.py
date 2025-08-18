from tkinter import *
import requests

URL = 'https://api.kanye.rest/'


def get_quote():
    response = requests.get(URL)
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=response.json()["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", border=0, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Pres icon for Quote", width=250, font=("Arial", 25, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="white", border=0)
kanye_button.grid(row=1, column=0)

window.mainloop()
