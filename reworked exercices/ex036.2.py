# Ex036.2
"""Write a program to approve the bank loan for the purchase of a house
Ask the value of the house, the buyer's salary and how many years he will pay
The monthly installment cannot exceed 30% of the salary or the loan will be denied"""

house_value = float(input('What is the value of the house?: '))
salary = float(input("What is the buyer's salary?: "))
financing = int(input('How many years of financing?: '))
salary30 = salary * 30 / 100
monthly = house_value / (financing * 12)
print(f'To buy a house of R$ {house_value:.2f} in {financing} years, the monthly installment will be R$ {monthly:.2f}')
if monthly >= salary30:
    print(f'LOAN DENIED!')
else:
    print('APPROVED LOAN!')
