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

def calculator():
    num1 = float(input("What's the first number: "))

    for key in operations:
        print(f"{key}")
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an opeartion: ")
        num2 = float(input("What's the next number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f" Type 'y' to calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()