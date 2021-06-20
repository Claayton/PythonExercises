# Ex049.2
"""Redo exercises 09 showing the multiplication table of a number that user choses, only now using a 'for' loop"""

number = int(input('Enter a number to see his multiplication table: '))
print(f'{"="}'*20)
print(f'\033[7:40m{"MULTIPLICATION TABLE"}\033[m')
print(f'{"="}'*20)
for table in range(1, 11):
    print(f'{number} X {table:>2} = {number * table:>2}')
print(f'{"="}'*20)
