#In this section we are going to create a calculator program

#Calculator

#Add
def add(n1,n2):
    return n1 + n2

#substract
def substract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#division
def division(n1,n2):
    return n1/n2

#operation
operations = {"+":add, "-":substract, "*":multiply, "/":division}

num1 = int(input("What's the first number: "))
num2 = int(input("What's the second number: "))

for key in operations:
    print(f"{key}")

operation_symbol = input("Pick an opeartion form the line above: ")

answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")