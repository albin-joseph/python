#In this section we are goin to leran about dictionary comprehension

# new_dict = {new_key:new_value for item in list}
import random

students = ["Albin", "Anu", "Emmanuel", "Rebecca"]
students_scores = {student:random.randint(1,100) for student in students}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


# Exercise : weekly climate temp report convert degree to FH
weather_report_in_Deg = {"Sunday": 23.5,"Monday": 23, "Tuesday": 25, "Wedensday": 24.5, "Thursday": 22, "Friday": 23, "Sataurday": 24}
weather_report_in_FH = {day:(temp*9/5)+32 for (day, temp) in weather_report_in_Deg.items()}
print(weather_report_in_Deg)
print('-------------------------------')
print(weather_report_in_FH)

