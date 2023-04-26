#In this section we learn more abou the python function.

def greet(name):
    print(f"Hello, {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")
    
greet("Albin")

#Parameter is the variable passing to the function
#argument is the actual value we are passing to the function

#A function to pass two arguments
def getFullName(firstName, lastName):
    print(f"My full name: {firstName} {lastName}")
    
getFullName("Albin", "Joseph")

#We can call function with parameter and arument. 
#It will look which argument associate with the parameter
#This will reduce the error prone situations
getFullName(firstName="Anu", lastName="Jose")


#Below program for calculate the area of a wall

def getTheArea(height, width):
    return height * width

areaOfWall = getTheArea(5,6.5)
print(f"Area of the wall is: {areaOfWall}")
