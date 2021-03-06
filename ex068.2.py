# Ex068.2
"""Make a program that plays even or odd with the computer.
The game will only be interrupted when the player LOSES,
Showing the total of consecutive victories that he won at the end of the game."""

from random import choice
choose = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 'WON'
while True:
  if result == 'LOST':
    break
  print('[1] ODD\n[2] EVEN')
  usu_choose = int(input('Make your choice: '))
    if usu_choose == 1:
      pc_choose = 2
    elif usu_choose == 2:
      pc_choose = 1
    else:
      print('')
  pc_choose = choice(choose)
