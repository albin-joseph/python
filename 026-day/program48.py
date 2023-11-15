# In this section we are going to learn how to create List using List comprehensions

# new_list = [new_item for item in list]

#Number
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)


#String
name = "Albin"
new_name_list = [letter for letter in name]
print(new_name_list)

#Range
# Double the values in the range
double_value_list = [n*2 for n in range(1,5)]
print(double_value_list)

#Do some operations
names = ["Anu", "Albin", "emmanuel", "Rebecca"]
short_names = [name for name in names if len(name) <= 5]
print(short_names)
# Print long names in uppper case
long_names =  [name.upper() for name in names if len(name) > 5]
print(long_names)

#Get list of squares from the number list
number_list = [1, 2, 11, 21, 24, 36, 55]
square_list = [n*n for n in number_list]
print(square_list)

#Accespt a list of number as comman separated strings and get the comprehensive list of even number
input_list = input("Enter numbers seperated with commas: ").split(',')
print(f"input_list: {input_list}")
new_number_list = [int(char) for char in input_list]
print(f"new_number_list: {new_number_list}")
odd_number_list = [n for n in new_number_list if n%2 != 0]
print(f"odd_number_list: {odd_number_list}")
even_number_list = [n for n in new_number_list if n%2 == 0 and n != 0]
print(f"even_number_list: {even_number_list}")





