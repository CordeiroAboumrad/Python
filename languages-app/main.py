from tkinter import *
import random
import pandas
import csv

BACKGROUND_COLOR = "#91C2AF"
word_in_portuguese = {}
to_learn = {}
random_word = {}

try:
    data_file = pandas.read_csv("./words/words_to_learn.csv")
except:
    data_file = pandas.read_csv("./words/Languages.csv")
    to_learn = data_file.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")


# ----------------------------------- PICK RANDOM WORD -------------------------------------------------
def pick_random_word():
    global word_in_portuguese, flip_timer, random_word
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    random_english_word = random_word["English"]
    word_in_portuguese = random_word["Portuguese"]
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=f"{random_english_word}", fill="black")
    canvas.itemconfig(card_foreground, image=foreground_image)
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    global random_word
    lista_dict = []
    lista_dict.append(random_word)
    print(lista_dict)
    words_data = pandas.DataFrame(lista_dict)
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words/words_to_learn.csv", index=False)
    try:
        with open("words/learnt_words.csv", "r"):
            print("The file exists.")
        # words_data.to_csv("words/learnt_words.csv", mode='a', index=False, header="column_names")
        words_data.to_csv("words/learnt_words.csv", mode='a', index=False, header=False)
    except:
        words_data.to_csv("words/learnt_words.csv", mode='w', header=True, index=False)

    pick_random_word()


# ------------------------------------- UI SETUP --------------------------------------------------------

def flip_card():
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=f"{word_in_portuguese}", fill="white")
    canvas.itemconfig(card_foreground, image=background_image)


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

foreground_image = PhotoImage(file="./images/card_front.png")
background_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526)
card_foreground = canvas.create_image(400, 263, image=foreground_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"Word", font=("Arial", 60, "italic"))

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=known_word)
known_button.grid(row=1, column=1)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=pick_random_word)
unknown_button.grid(row=1, column=0)

pick_random_word()

window.mainloop()
