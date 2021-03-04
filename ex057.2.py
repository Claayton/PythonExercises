# Ex057.2
"""Make a program that reads the gender of a person, but only accepts the values 'M' of 'F'.
If it is wrong, ask for the typing again until it has a correct value."""

from time import sleep
sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Please inform your gender [M/F]: ')).upper()
print('Loading', end=''), sleep(0.5)
print('.', end=''), sleep(0.5)
print('.', end=''), sleep(0.5)
print('.')
if sex == 'M':
    print('\033[32mMale registered\033[m')
elif sex == 'F':
    print('\033[32mFamale registered\033[m')
