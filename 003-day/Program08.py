#The expression inside the indentation called block of code. If anything declare will have scope in that only.
# These are the comparison operators are <, > <=, >=, ==, !=

height = int(input("What is your height? "))

if height > 120:
    print("You can use rollercoaster")
else:
    print("You can not use rollercoaster")
    
#sample program to find out a number is odd or even

number = int(input("Please enter a value greater than zero: "))

if number // 2 == 0:
    print(f"{number} is an even number")
else:
   print(f"{number} is an odd number")