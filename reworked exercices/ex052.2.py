# Ex052.2
""" Make a program that reads an integer and tells you whether or not it is a prime number"""

cont = 0
cont_prime = 0
prime = ''
number = int(input('Enter a number: '))
for p in range(1, number + 1):
    cont += 1
    if number % cont == 0:
        print('\033[31m', end='')
        cont_prime += 1
    print(p, '\033[m', end='')
if cont_prime == 2:
    prime = '\033[32mPRIME\033[m'
else:
    prime = '\033[31mNOT PRIME\033[m'
print(f'\nThe number \033[32m{number}\033[m was divisible \033[32m{cont_prime}\033[m times')
print(f'So it is {prime}')
