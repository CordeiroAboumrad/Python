from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("My first GUI Program")
window.config(padx=10, pady=10)

# Label
my_label = Label(text="I am a label", font=("Arial", 18, "bold"))
my_label.pack()
my_label.grid(column=0, row=0)

# my_label["text"] = "I am a modified label!"
# my_label.config(text="New Text")

# Button
clicks = 0


def button_clicked():
    global clicks
    clicks += 1
    # my_label["text"] = f"I got clicked {clicks} times"
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_clicked)
# Pack method includes elements in the screen
button.grid(column=1, row=1)

button2 = Button(text="Click Here", command=button_clicked)
button2.grid(column=2, row=0)

input = Entry()
input.config(justify="center")
input.grid(column=3, row=2)

text = Text(height=2.5, width=30)
# Puts cursor in the textbox
text.focus()
# Adds some initial text
text.insert(END, "Example")
# Gets current value in textbox at line 1,character 0
print(text.get("1.0", END))


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)


# Scale

# Called with current scale value
def scale_used(value):
    # print(scale.get())
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)


# Checkbutton
# Prints 1 if on button is checked; otherwise,0.
def checkbutton_used():
    if checked_state.get() == 1:
        print("On")
    else:
        print("Off")


checked_state = IntVar()
checkbutton = Checkbutton(text="adicionar", variable=checked_state, command=checkbutton_used)


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)


# Listbox
def listbox_used(event):
    # Gets current selection from list
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)

window.mainloop()
