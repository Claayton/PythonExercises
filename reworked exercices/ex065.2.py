# Ex065.2
"""Create a program that reads several integers from the keyboard.
At the end of the run, show the average of all values and which was the highest and lowest values read.
The program should ask the user whether or not he wants to continue to the values."""

again = 'S'
cont = 0
sum = 0
while again == 'S':
  number = int(input('Type a number: '))
  again = str(input('Do you want to continue?: ')).upper().strip()
  cont += 1
  sum += number
  if cont == 1:
    highest = number
    lowest = number
  if number > highest:
    highest = number
  if number < lowest:
    lowest = number
average = sum / cont
print('-' * 50)
if again != 'N' and again != 'S':
  print('\033[31mINVALID OPTION, TRY AGAIN\033[m')
else:
  print(f'The average between {cont} values entered is {average:.2f}')
  print(f'The highest number is {highest}')
  print(f'The lowest number is {lowest}')
