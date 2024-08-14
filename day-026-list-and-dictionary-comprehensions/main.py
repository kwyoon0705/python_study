import random

# List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)

# Dictionary Comprehension
students_scores = {name: random.randint(1, 100) for name in names}
passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)
