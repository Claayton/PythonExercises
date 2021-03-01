# Ex054.2
"""Create a program that reads the year of birth of seven people, at the end,
Show how many people are not yet of age and how many are already older"""

from datetime import date

current_year = date.today().year
adulthood = 0
minority = 0

for y in range(0, 7):
    year_of_birth = int(input(f'What is the birth year of the {y + 1}° person?: '))
    if year_of_birth + 18 <= current_year:
        adulthood += 1
    else:
        minority += 1
print(f'Of the 07 registered people, {adulthood} are of legal age, and {minority} are minors')
