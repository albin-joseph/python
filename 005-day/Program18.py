# Create a strong passsword. Password shoud contain user suggested number of letters, symbols and numbers
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ';', ';', ':',',','.', '?', '|']

number_of_letters = int(input("How many letters would you like to add in your password? "))
number_of_numbers = int(input("How many numbers would you like to add in your password? "))
number_of_symbols = int(input("How many symbols would you like to add in your password? "))

password_list = []

for n in range(0, number_of_letters):
    password_list.append(random.choice(letters))

for n in range(0, number_of_numbers):
    password_list.append(random.choice(numbers))
    
for n in range(0, number_of_symbols):
    password_list.append(random.choice(symbols))
    
random.shuffle(password_list)

password = ""

for item in password_list:
    password += item

print(f"Suggested password is {password}")