#In this section we send motivational email on every Monday
import os
import random
import smtplib
import datetime as dt

def send_email(quote):
    my_email = "my_email@gmail.com"
    password = "******"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="to_email@gmail.com", msg=f"subject:Monday Motivation\n\n {quote}")

with open(f"{os.getcwd()}/032-day/quotes.txt") as file:
    quotes = file.readlines()

selected_quote = random.choice(quotes)

today = dt.datetime.now()
if(today.weekday() == 0):
     send_email(selected_quote)
