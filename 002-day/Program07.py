# This program to calculate per person contribution on bill
# In this we can learn dtatypes, type cast, aritmentic operations and format the value.

bill = float(input("What was your bill amount? "))
tip_percentage = float(input("How much are you planning to give as tip(in percentage 10, 12 or 15)? "))
total_persons = int(input("How many members are you? "))

tip_amount = bill * (tip_percentage/100)
net_amount = tip_amount + bill
per_person_contribution = net_amount / total_persons
formated_contribution_amount = "{:.2f}".format(per_person_contribution)

print(f"Each persion should pay {formated_contribution_amount}")
