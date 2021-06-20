# Ex041.2
"""The National Swimming Confederation needs a program that reads the year of birth of an athlete,
And shows his category, according to age:
Up to 9 years: Child
Up to 14 years old: Children
Up to 19 years old: Junior
Up to 25 years old: Senior
Above: Master
"""

from datetime import date
year_of_birth = int(input('What is the year of birth?: '))
current_year = date.today().year
age = current_year - year_of_birth
print(f'The athlete is {age} years old')
Category = ''
if age <= 9:
    category = 'Child'
elif age <= 14:
    category = 'Children'
elif age <= 19:
    category = 'Junior'
elif age <= 25:
    category = 'Senior'
else:
    category = 'Master'
print(f'Category: {category}')
