# Ex067.2
"""Make a program that shows the multiplication table of several numbers one at a time,
For each value entered by the user.
The program will be interrupted when the requested number is negative."""

number = int(input('Enter a number to see his multiplication table: '))
while True:
  if number < 0:
    break
  print(f'{"="}'*20)
  print(f'\033[7:40m{"MULTIPLICATION TABLE"}\033[m')
  print(f'{"="}'*20)
  for table in range(1, 11):
      print(f'{number} X {table:>2} = {number * table:>2}')
  print(f'{"="}'*20)
  number = int(input('Enter a number to see his multiplication table: '))
print('\033[32mNegative numbers end the program\nThanks for using!\033[m')
