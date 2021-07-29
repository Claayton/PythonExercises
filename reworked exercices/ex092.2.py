# Ex092.2
"""Create a program that reads name, year of birth and work card and registers (with age) in a dictionary, if by choice the CTPS is different from ZERO, the dictionary will also receive the year of employment and salary.
Calculate and add, in addition to age, how old the person will retire at."""

from datetime import date

person = {}
today = date.today().year

print('\033[35m><\033[m' * 30)
person['Name'] = str(input('\033[36mName: \033[m').title().strip())
bird = int(input('\033[36mYear of bird: \033[m'))
person['Age'] = today - bird
person['CTPS'] = int(input('\033[36mWork Card: [0 if you do not have]: \033[m'))
if person['CTPS'] != 0:
    person['Hiring'] = int(input('\033[36mYear of hiring: \033[m'))
    person['Wage'] = float(input('\033[36mWage: \033[m'))
    hiring_age = person['Hiring'] - bird
    person['Retirement'] = hiring_age + 35

print('\033[35m><' * 30)
for c, i in person.items():
    print(f'\033[36m{c} \033[mhave the value \033[36m{i}\033[m')
print('\033[35mxD\033[m')
