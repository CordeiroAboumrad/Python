import datetime as dt
import random
import smtplib
import pandas

my_email = os.environ.get(EMAIL)
password = os.environ.get(PASSWORD)
used_quotations = []

today = dt.datetime.today()
weekday = today.weekday()
print(today)
print(weekday)

with open("quotes.txt") as file:
    quotations_list = file.readlines()

# Checking if it's Monday
if weekday == 5:
    random_quotation = random.choice(quotations_list)
    quotations_list.remove(random_quotation)
    random_quotation = random_quotation.rstrip()
    used_quotations.append(random_quotation)
    df_used_quotations = pandas.DataFrame(used_quotations)
    try:
        with open("quotations/used_quotations.csv", "r"):
            df_used_quotations.to_csv("quotations/used_quotations.csv", mode='a', index=False, header=False)
    except:
        df_used_quotations.to_csv("quotations/used_quotations.csv", mode='w', index=False, header=False)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=os.environ.get(EMAIL2),

                            msg=f"Subject:Frase da Semana\n\n{random_quotation}")
