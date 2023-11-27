#Please follow the following step  for send mail
# 1. create a new gmail account
# 2. Enable 2 step varification
# 3. Create an app password
# 4. That app password add it as password in our program

import smtplib

my_email = "mygmail@gmail.com"
password = "*******"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="my_another@gmail.com", msg="subject:Hello\n\n This is the body of the email")
