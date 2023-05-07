#Dictionary   

#Its's the combination of key-value pair.Every dictionary has two thing key and value. Value is always associated with a key.
#Eg: {"name": "Albin"}. In this key is name and Albin is value

empty_dictionary = {}

students_name = {"name": "Albin"}
students_name["name"] = "Anu"
print(students_name)

#We can iterarte by for loop

for key in students_name:
    print(key)
    print(students_name[key])
    
#Create program with students name and their grade
student_scores = {
    "Albin": 98,
    "Anu": 80,
    "Arsha": 75,
    "Atul": 80
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Excellent"
    elif score >= 80:
         student_grades[student] = "Best"
    elif score >= 70:
         student_grades[student] = "Good"
    else:
        student_grades[student] = "Need to improve"

print(student_grades)