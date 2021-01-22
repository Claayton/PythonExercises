#Ex007.2
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

grade1 = float(input("What was the student's first grade?: "))
grade2 = float(input("What was the student's second grade?: "))
average = (grade1 + grade2) / 2
print(f'The average between {grade1} and {grade2} is equal to {average}')
