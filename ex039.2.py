# Ex039.2
"""Make a program that reads the year of birth of a young person and informs them, acoording to they age
If they are still going to apply for military service,
If it is time to enlist,
Or if they are past the time of enlistment
Your program should also show the time left or past the deadline"""
from datetime import date
year_of_birth = int(input('What is your year of birth?: '))
current_year = date.today().year
age = current_year - year_of_birth
print(f'Who was born in {year_of_birth} is {age} years old in {current_year}')
if age < 18:
    print(f'There are still {18 - age} years before your enlistment')
    print(f'Your enlistment will be {year_of_birth + 18} years from now')
elif age > 18:
    print(f'His enlistment was {age - 18} years ago')
    print(f'His enlistment was in {year_of_birth + 18}')
elif age == 18:
    print('Your enlistment is this year, stay tuned!')
print()
