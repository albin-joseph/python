#HOF
#Higher order function is called a function that take a function as parameter and perform that function inside the function and return the result

#State
#Each Object/Instance have their on property value. This property value is call State.

#Example of higher order function

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def calculator(x, y, func):
    return func(x,y)

print(calculator(3,2,add))
print(calculator(10,5, multiply))

#In the above `calculator` function is the higher order function 