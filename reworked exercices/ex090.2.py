# Ex090.2
"""Make a program that reads a student's name and average, also saving the situation in a dictionary.
At the end, show the content os the structure on the screen."""

student = {}

name = str(input('\033[32mName: \033[m').strip().title())
student['Name'] = name
average = float(input(f'\033[32mAverage of {name}: \033[m'))
student['Average'] = average
if average <= 5:
    student['Situation'] = 'Disapproved'
elif average < 7:
    student['Situation'] = 'Recuperation'
elif average >= 7:
    student['Situation'] = 'Approved'
print('\033[31m=\033[m' * 40)
for k, v in student.items():
    print(f'\033[32m{k} \033[34mé igual a \033[32m{v}\033[m')
print('\033[31m=\033[m' * 40)
print('\033[32mxD\033[m')
