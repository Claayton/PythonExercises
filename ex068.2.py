# Ex068.2
"""Make a program that plays even or odd with the computer.
The game will only be interrupted when the player LOSES,
Showing the total of consecutive victories that he won at the end of the game."""

from random import randint
final_result = 'WON'
cont = 0
while True:
  if final_result != 'WON':
    break
  print('\033[7m[0] EVEN \033[m\n\033[7m[1] ODD  \033[m')
  usu_choose = int(input('Make your choice: '))
  if usu_choose == 0:
    pc_choose = 1
  else:
    pc_choose = 0
  print(f'You choice \033[32m{usu_choose}\033[m, and PC choose \033[32m{pc_choose}\033[m')
  usu_number = int(input('Choose your number: '))
  pc_number = randint(0, 10)
  print(f'You choose \033[32m{usu_number}\033[m and the PC choose \033[32m{pc_number}\033[m')
  if usu_choose == 0:
    if usu_number + pc_number % 2 == 0:
      print('\033[31mWON, PLAY AGAIN\033[m')
      final_result = 'Won'
      cont += 1
    else:
      print('\033[31mLOST SUCKER\033[m')
      final_result = 'LOST'
  if usu_choose == 1:
    if usu_number + pc_number % 2 == 1:
      print('\033[32mWON, PLAY AGAIN\033[m')
      final_result = 'Won'
      cont += 1
    else:
      print('\033[31mLOST SUCKER\033[m')
      final_result = 'LOST'
print(f'\033[32mYou WON {cont} times.\033[m')
# não terminei ainda essa merda dos infernos puta que pariu, da primeira que eu fiz foi facil, agora t dificil