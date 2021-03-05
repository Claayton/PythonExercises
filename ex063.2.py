# Ex063.2
"""Write a program that reads a number and integer 'n',
And show on the screen the 'n' first elements of a fibonacci sequence.
Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8."""

cont = 0
fib = 0
fib2 = 0
print('Fibonacci Sequence')
first = int(input('How many numbers you want to show?: '))
while cont < first:
    cont += 1
    fib = first
    fib2 = fib + first
    fib = fib2
    print(fib, end='\033[31m>\033[m')
# ainda não terminei esse desculpa