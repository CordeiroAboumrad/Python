from tkinter import *

window = Tk()
window.minsize(width=200, height=30)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def button_clicked():
    miles = input.get()
    miles = miles.replace(",", ".")
    kilometers = float(miles) * 1.6
    dynamic_label["text"] = kilometers


# Text input
input = Entry(width=10)
input.config(justify="center")
input.insert(END, 0)
input.grid(row=0, column=1)

# Label 0
miles_label = Label(text="miles", font=("Arial", 10), justify="center")
miles_label.grid(row=0, column=2)

# Label 1
conversion_label = Label(text="is equal to", font=("Arial", 10), justify="center")
conversion_label.grid(row=1, column=0)

# Label 2
dynamic_label = Label(text=0, font=("Arial", 12, "bold"), justify="center")
dynamic_label.grid(row=1, column=1)

# Label 3
kilometers_label = Label(text="Km", font=("Arial", 10), justify="center")
kilometers_label.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
