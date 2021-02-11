# Ex043.2
"""Develop a logic that reads the weight and height of a person,
Calculate his BMI and show his status, according to the table bellow:
Under 18.5: Underweight
Between 18.5 and 25: Ideal weight
25 to 30: Overweight
30 to 40: Obese
Over 40: Morbidly obese"""

weight = float(input('What is your weight? (kg): '))
height = float(input('How tall are you? (m): '))
bmi = weight / (height * height)
print(f'This person BMI is {bmi:.1f}')
if bmi < 18.5:
    print('CAUTION, Are you overweight')
elif 18.5 <= bmi < 25:
    print('CONGRATULATIONS, you are at your ideal weight')
elif 25 <= bmi < 30:
    print('Are you overweight')
elif 30 <= bmi < 40:
    print('CAUTION, Are you obese')
elif bmi > 40:
    print('Go diet fatso, Are you morbidly obese')
