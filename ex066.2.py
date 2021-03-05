# Ex066.2
"""Create a program that reads several integers from the keyboard.
The program will only stop when the user types '999', which is the stop condition.
At the end, show how many numbers were entered and what was the sum beteween them (disregarding the flag)."""

num = 0
cont = 0
sum = 0
print('\033[41m[999] TO STOP AT ANY TIME \033[m ')
while True:
  num = int(input('Type a number: '))
  if num == 999:
    break
  cont += 1
  sum += num
print('\033[41m-\033[m' * 26)
print(f'You typed {cont} numbers')
print(f'The sum between ther are {sum}')
