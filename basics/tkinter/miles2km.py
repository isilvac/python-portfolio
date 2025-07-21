from tkinter import Tk, Entry, Button, Label

FONT = ("Nunito Sans", 20)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


def calculate_km():
    amount_label.config(text=f"{(float(miles_input.get()) / 1.609):.1f}")


miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)
label1 = Label(text="Miles", font=FONT)
label1.grid(row=0, column=2)

label2 = Label(text="is equal to", font=FONT)
label2.grid(row=1, column=0)
amount_label = Label(text="", font=FONT)
amount_label.grid(row=1, column=1)
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)

window.mainloop()
