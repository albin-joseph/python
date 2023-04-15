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

print(6 + 4 / 2 - (1 * 2))


#A program to find out the BMI value
#BMI =  weight/heigh*height

height = input("Please enter your height: ") 
weight = input("Please enter your weight: ")

pre_bmi = float(weight)/(float(height) ** 2)

bmi = int(pre_bmi)

print("Your BMI is: " + str(bmi))

# Modulas operation is done by //

abs_value = 6 // 4
print(abs_value)

# Ther is short hand feature available in python. Please find some examples

score = 0
print(score)
score += 5
print(score)
score -= 2
print(score)
score *= 3
print(score)
score /= 2
print(score)
score //= 4
print(score)

# Print all type of values in to a string by appending f value befor print item
isPrint = True
print(f"{score}, {isPrint}")