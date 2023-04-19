#In this section we are going to leran about functions in Python.

#Define a function in python by using a key word def
#After def key word  function name and column
#Then inside the block we can write the expression belongs to the function
#We need to ensure the indentation added correctly.

def my_function():
    print("my_function executed")
    
my_function()

#Advantage of using functios:
    #Code is more readable
    #Reuse the code & Reduce number of lines in our program
    #Bring modularity
    
# write a function to find out the sum of two intigers

def sum(a,b):
    return a + b

result = sum(3,9)

print(result)

def multiply(x,y):
    return x * y

print(multiply(7,3))
