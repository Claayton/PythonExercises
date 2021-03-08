# Ex068.2
"""Make a program that plays even or odd with the computer.
The game will only be interrupted when the player LOSES,
Showing the total of consecutive victories that he won at the end of the game."""

from random import randint
cont = 0
while True:
  print(f'\033[7;30;47m{"EVEN [0]":^25}\033[m\n\033[7;30;47m{"ODD [1]":^25}\033[m')
  usu_choose = int(input('Make you choice: \033[32m'))
  if usu_choose == 0:
    usu_choose = 'EVEN'
    pc_choose = 'ODD'
  elif usu_choose == 1:
    usu_choose = 'ODD'
    pc_choose = 'EVEN'
  else:
    print(f'\033[1;31;40m{"INVALID CHOICE":^25}\033[m')
    break
  print(f'\033[mYou chose: \033[32m{usu_choose}\033[m\nPC chose: \033[32m{pc_choose}\033[m')
  print(f'\033[40m{" ":^25}\033[m')
  usu_number = int(input('You choose the number: \033[32m'))
  pc_number = randint(0, 10)
  print(f'\033[mPC choose the number: \033[32m{pc_number}\033[m')
  sum = usu_number + pc_number
  if sum % 2 == 0:
    result = 'EVEN'
  else:
    result = 'ODD'
  print(f'The sum is: \033[32m{sum}\033[m (\033[32m{result}\033[m)')
  if usu_choose == result:
    print(f'\033[1;32;40m{"WON, PLAY AGAIN":^25}\033[m')
    cont += 1
  else:
    print(f'\033[1;31;40m{"LOST SUCKER":^25}\033[m')
    break
print(f'\033[32mYou WON {cont} times.\033[m')
