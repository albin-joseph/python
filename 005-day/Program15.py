#In this section we are going to leran more about Loops.
#Loop using lists

fruits = ["apple", "manago", "orange", "pineapple"]

for fruit in fruits:
    print(fruit)

# We can use the same iteration logic in the case of string also
strs = "abcdefg"
for str in strs:
    print(str)

#NB: When we using the loops we need to ensure the indentation and block of code is correct.

#Find the average height of the students from the lists
students_heights = [50, 55, 57, 65, 70, 51, 53]

total_height = 0
for height in students_heights:
    total_height += height

average_height = "{:.2f}".format(total_height/len(students_heights))

print(f"Average height is: {average_height}")

#By using the range function we can list the values between the range

#print numbers between 1 to 10
for number in range(1, 10):
    print(number)
    
#We can add a step varibale in rnge function
#Print numbers which divisible by 5 between 0 and 50
for n in range(0, 50, 5):
    print(n)

