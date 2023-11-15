#In this program we read the numbers from the text file and find the common numbers occur in the files
import os

with open(f"{os.getcwd()}/026-day/file1.txt") as file1:
    list_1 = file1.readlines()
    print(list_1)
    
with open(f"{os.getcwd()}/026-day/file2.txt") as file2:
    list_2 = file2.readlines()
    print(list_2)
    
result = [int(num) for num in list_1 if num in list_2]
print(result)