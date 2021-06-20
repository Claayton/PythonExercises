# Ex064.2
"""Create a program that reads several integers from the keyboard.
The program will only stop when the user enters the value '999', wich is the stop condition.
At the end, show how many numbers were entered and what was the sum between them (disregarding the flag)."""

num = 0
cont = - 1
sum = - 999
print('\033[41m[999] TO STOP AT ANY TIME \033[m ')
while num != 999:
  num = int(input('Type a number: '))
  cont += 1
  sum += num
print('\033[41m-\033[m' * 26)
print(f'Were digitizer {cont} numbers')
print(f'The sum between them are {sum}')
