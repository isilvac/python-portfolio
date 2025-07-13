import json
from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage, END, messagebox

import pyperclip

from generator import generate_password

FONT_NAME = "Nunito Sans"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_password():
    pass_input.delete(0, END)
    proposed = generate_password()
    pass_input.insert(0, proposed)
    pyperclip.copy(proposed)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    site = website_input.get()
    try:
        with open("data/data.json", "r") as credentials_file:
            data = json.load(credentials_file)
    except FileNotFoundError:
        messagebox.showinfo(title="{site}", message="No Data File found")
    if site in data:
        messagebox.showinfo(title="{site}", message=f"Data for {site}:\n"
                                                    f"User:{data[site]["email"]}\nPassword:{data[site]["password"]}")
    else:
        messagebox.showinfo(title="{site}", message=f"No details for {site} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = website_input.get()
    user = user_input.get()
    pasw = pass_input.get()
    new_data = {site: {"email": user, "password": pasw}}

    if len(site) < 1 or len(user) < 1 or len(pasw) < 1:
        messagebox.showerror(title="Oops!", message="You forgot some data...🤦🏻")
    else:
        messagebox.showinfo(title="{site}",
                            message=f"This data for {site} is being saved:\n user:{user}\npassword:{pasw}")
        try:
            with open("data/data.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            with open("data/data.json", "w") as write_file:
                json.dump(new_data, write_file, indent=4)
        else:
            data.update(new_data)
            with open("data/data.json", "w") as write_file:
                json.dump(data, write_file, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas and logo
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="data/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:", font=(FONT_NAME, 20))
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1, sticky="W")
website_input.focus()

search_button = Button(text="Search", command=find_password, font=(FONT_NAME, 15), width=14)
search_button.grid(row=1, column=2, sticky="W")

# User
user_label = Label(text="Username/email:", font=(FONT_NAME, 20))
user_label.grid(row=2, column=0)

user_input = Entry(width=41)
user_input.grid(row=2, column=1, columnspan=2, sticky="W")
user_input.insert(0, "john.doe@gmail.com")

# Password
pass_label = Label(text="Password:", font=(FONT_NAME, 20))
pass_label.grid(row=3, column=0)

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1, sticky="W")

pass_button = Button(text="Generate Password", command=new_password, font=(FONT_NAME, 15))
pass_button.grid(row=3, column=2, sticky="W")
# Add button
add_button = Button(text="Add", width=34, command=save_password, font=(FONT_NAME, 15))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
