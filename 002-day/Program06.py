#Aritmetic operationas and details about the order of execurion
#The arithemntic operation python happend from Left to Right
#The priority of operation is based on the rule PEMDASLR

# paranthesis : ()
# Exponential or Power : **
# Multiplication : *
# Division : /
# Addition : +
# Substraction : -
#Execution of above operation will happen from Left to Right 

#To see the results
print(3*3+3/3-3)
print(3/3+3-3*3)
print((3/3)+3*3-3)
print(3/(3+3)*3-3)


#A program to find out the BMI value
#BMI =  weight/heigh*height

height = input("Please enter your height: ") 
weight = input("Please enter your weight: ")

pre_bmi = float(weight)/(float(height) ** 2)

bmi = int(pre_bmi)

print("Your BMI is: " + str(bmi))