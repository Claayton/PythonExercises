# Ex034.2
"""Write a program that asks for an employer's salary and calculates the amount of their increase,
For salaries greater than R$ 1250.00, calculate an increase of 10%
For less than of equals, the increases is 15%"""

salary = float(input("What is the employee' salary? "))
if salary > 1250:
    increase = 10
else:
    increase = 15
print(f'Whoever received R$: {salary:.2f}, starts to receive R$: {salary + ((salary * increase) / 100):.2f}')
