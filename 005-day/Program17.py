#find the largest number in a list

numbers = [50, 55, 39, 45, 20, 67, 70, 23, 58, 76, 90, 24, 69]

largest_number = numbers[0]

for number in numbers:
    if(largest_number < number):
        largest_number = number

print(f"Largest number in the list is: {largest_number}")