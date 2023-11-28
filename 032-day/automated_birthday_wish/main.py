import os
import pandas
import datetime as dt
import smtplib
from tkinter import *
import random

my_email = "test@gmail.com"
password = "******"


# ---------------------------- SEND EMAIL ------------------------------#
def send_email(content, to_email, name):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"subject:Happy birthday {name}\n\n {content}")

# ---------------------------- PREPARE EMAIL DRAFT ------------------------------#
def draft_email(person_record):
    letter_id = random.randint(1, 3)
    with open(f"{os.getcwd()}/032-day/automated_birthday_wish/letter_templates/letter_{letter_id}.txt", "r") as template:
        content = template.read()
        updated_content = content.replace('[NAME]', person_record["name"])
        send_email(updated_content, person_record["email"], person_record["name"])


#------------------------------------ CHECK BIRTHDAY -----------------------------#
def check_birth_day():
    df = pandas.read_csv(f"{os.getcwd()}/032-day/automated_birthday_wish/birthdays.csv")
    dict = df.to_dict(orient='records')
    
    today = dt.datetime.now()
    month = today.month
    day = today.day
    
    for person_record in dict:
        if person_record["month"] == month and person_record["day"] == day:
            draft_email(person_record)
    
 
 
       
check_birth_day()



