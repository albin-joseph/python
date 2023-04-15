#The expression inside the indentation called block of code. If anything declare will have scope in that only.
# These are the comparison operators are <, > <=, >=, ==, !=

height = int(input("What is your height? "))

if height > 120:
    print("You can use rollercoaster")
else:
    print("You can not use rollercoaster")
    
#sample program to find out a number is odd or even

number = int(input("Please enter a value greater than zero: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
   print(f"{number} is an odd number")
   
#To check an Year is Leap year

year = int(input("Please enter an year: "))

if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
#We can create nested if statements and also by using elif statement
#Please find the examples below

print("Please check the value is divisible by 2,3 or 5")
value = int(input("Please enter a number: "))

if value % 2 == 0:
    print(f"{value} is divible by 2")
elif value % 3 == 0:
     print(f"{value} is divible by 3")
elif value % 5 == 0:
     print(f"{value} is divible by 5")
else:
    print(f"{value} is not divible by 2,3 or 5")