# Ex056.2
"""Develop a program that reads the name, age and sex of for people. At the end of the program, show:
The average age of the group,
What's the name of the older man,
How many women are under 20"""

total_age = 0
older_man = 0
name_over_man = ''
women20_cont = 0
for n in range(1, 4 + 1):
  print(f'\033[32mPerson number {n}\033[m')
  name = str(input('What is the name?: ')).title()
  age = int(input('What is the age?: '))
  sex = str(input('What is the sex? [M /F]: ')).upper()
  total_age += age
  if sex == 'M' and age > older_man:
    older_man = age
    name_older_man = name
  if sex == 'F' and age < 20:
    women20_cont += 1
  print('\033[31m-\033[m' * 30)
average_age = total_age / 4
print(f'The average age of the group is \033[32m{average_age}\033[m')
print(f'The name of the older man is \033[32m{name_older_man}\033[m with \033[32m{older_man}\033[m years old')
print(f'Women under 20: \033[32m{women20_cont}\033[m')
