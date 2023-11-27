#In this section we send motivational email on every Monday
import os
import random
import smtplib
import datetime as dt


with open(f"{os.getcwd()}/032-day/quotes.txt") as file:
    quotes = file.readlines()

selected_quote = random.choice(quotes)

today = dt.datetime.now()
if(today.weekday() == 0):
     print('Today is Monday', selected_quote)
