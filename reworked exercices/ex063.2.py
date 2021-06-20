# Ex063.2
"""Write a program that reads a number and integer 'n',
And show on the screen the 'n' first elements of a fibonacci sequence.
Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8."""

cont = 0
fib = 0
fib2 = 0
fib3 = 0
print('Fibonacci Sequence')
first = int(input('How many numbers you want to show?: '))
print('-'* 50)
print(fib, end='\033[31m > \033[m')
while cont != first - 1:
  cont += 1
  if cont == 1:
    fib = 1
  fib3 = fib + fib2
  print(fib3, end='\033[31m > \033[m')
  fib = fib2
  fib2 = fib3
print('xD')
