#print pattens samples
row_count = int(input("How many row required? "))

print("TRIANGLE")
for i in range(1, row_count+1):
    str = ""
    for j in range(1, i+1):
        str += " * "
    print(str)
    
print("PYRAMID")
double_count = row_count*2
for i in range(0, row_count+1):
    str = ""
    for j in range(0, double_count):
        if j > int(double_count/2) - i and j < int(double_count/2) + i:
            str += "*"
        else:
            str += " "
    print(str)