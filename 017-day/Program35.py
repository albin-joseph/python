#in this section we are going to learn more about create a Class, Objects, etc
#Class name should be in Pascal cases
#Attribute is variables that associate with the class
#Constructor is special function in python which can understand python interpreter.
#Constructor uses for initialize the class
#Init fuction will call every time when we create an object

class User:
    def __init__(self, name):
        self.name = name

user1 = User("Albin")
print(user1.name)

