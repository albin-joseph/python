#in this section we are going to learn more about create a Class, Objects, etc
#Class name should be in Pascal cases
#Attribute is variables that associate with the class
#Constructor is special function in python which can understand python interpreter.
#Constructor uses for initialize the class
#Init fuction will call every time when we create an object

#Attributes are the things the object has
#Methods are the things the object does


class User:
    def __init__(self, name):
        self.name = name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        self.followers += 1
        user.following += 1

user_1 = User("Albin")
user_2 = User("Ajesh")
print(user_1.name)

user_1.follow(user_2)

print(f"{user_1.name} followers: {user_1.followers} & followng: {user_1.following}")
print(f"{user_2.name} followers: {user_2.followers} & followng: {user_2.following}")

