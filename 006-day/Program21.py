# In thi section we will learn more about while loop
# While loop will execute util the expression become false

print("Print 1 to 10")
number = 0
while number < 10:
    number+=1
    print(number)
    
print("Fibanoci series")

prev_value = 0
value = 1

number_of_values = int(input("How many fibbanoci numbers need to print: "))

count = 0
fibbanoci_series = ""

while count < number_of_values:
    fibbanoci_series += f" {value}"
    temp = value
    value += prev_value
    prev_value = temp
    count += 1

print(fibbanoci_series)
