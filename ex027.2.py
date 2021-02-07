# Ex027.2
"""Make a program that reads a person's full name, then show the first and last names separately"""

name = str(input('Enter a name: ')).title().strip()
name = name.split()
print(f'Your first name is {name[0]}')
print(f'And your last name is {name[-1]}')
print(f'Nice to meet you {name[0]}')
