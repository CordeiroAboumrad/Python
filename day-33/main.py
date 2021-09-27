# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# position = data["iss_position"]
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# coordinates = (latitude, longitude)
#
# print(data)
# print(coordinates)

from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    answer = response.json()
    quote = answer["quote"]
    print(quote)
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=20)

canvas = Canvas(width=600, height=828)
background_img = PhotoImage(file="images/background.png")
canvas.create_image(300, 414, image=background_img)
quote_text = canvas.create_text(300, 414, text="Kanye Quote Goes HERE", width=300, font=("Arial", 12, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="images/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=0, column=1)

window.mainloop()
