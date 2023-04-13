#In this section we are going to learn to more about Data Types
#In python these are the data types String, Intiger, Float & Boolean
# As any other languages operation between same data types only allow in Python.
#If any operation we have to do between two data types we need to cast the one of the varibale type to the type of the other variable.

#Intiger convert to string and print it

number_of_char = len(input("What is your name?\n"))
str_number_of_char = str(number_of_char)
print("Your name contains " + str_number_of_char + " characters.")

#Know the data type of a vriable by using type function

num = 275
print(type(num))
#Type cast in to string
str_num = str(num)
print(type(str_num))
