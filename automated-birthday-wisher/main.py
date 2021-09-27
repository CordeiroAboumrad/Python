import smtplib
import pandas
import random
import os
from datetime import datetime

login = os.environ.get(EMAIL)
password = os.environ.get(PASSWORD)

birthdays = pandas.read_csv("dates/birthday_dates.csv")
birthdays_dictionary = birthdays.to_dict(orient="records")
# print(birthdays_dictionary)

today_day = datetime.today().day
today_month = datetime.today().month


def send_email(birthday):
    random_letter = random.choice(os.listdir("letters"))
    with open(f"letters/{random_letter}", "r") as opened_letter:
        letter_content = str(opened_letter.read())
        letter_content = letter_content.replace("[NAME]", birthday["name"])
        # letter_content = letter_content.encode('ascii')
        print(letter_content)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=login, password=password)
            connection.sendmail(from_addr=login, to_addrs=birthday["email"],
                                msg=f"Subject: FELIZ ANIVERSARIO!\n\n{letter_content}")


for birthday in birthdays_dictionary:
    if birthday["month"] == today_month and birthday["day"] == today_day:
        person = birthday["name"]
        print(f"{person}'s birthday!")
        send_email(birthday)
