#Ex007.2
"""Develop a program that reads a student's two grades, calculates and displays his average"""

grade1 = float(input("What was the student's first grade?: "))
grade2 = float(input("What was the student's second grade?: "))
average = (grade1 + grade2) / 2
print(f'The average between {grade1} and {grade2} is equal to {average}')
