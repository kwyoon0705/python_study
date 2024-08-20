import random
import pandas

# List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)

# Dictionary Comprehension
students_scores = {name: random.randint(1, 100) for name in names}
passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(students_scores)
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [55, 100, 89]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    print(row.score)
