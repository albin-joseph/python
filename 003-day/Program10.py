# In this section we are going to learn about logical operators

#There are 3 types of logical operators

# and : If all the condition is satisfied, then this will return  true
# or : If either on of the condition is satisfied, then this will return  true
# not: It will return the inverse of the true or false

print("Check your category in school sports")
age = int(input("Enter your age: "))

if age < 6:
    print("Your category is Kids")
if age > 6 and age < 12:
    print("Your category is Junior")
if age > 12 and age < 18:
    print("Your category is Senior")
else:
    print("You are not eligible for participating the evenr.")