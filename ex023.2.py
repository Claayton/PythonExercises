# Ex023.2
"""Make a program that reads a number from 0 to 9999, and shows each separate digit on the screen"""

number = str(input('Enter a number: '))
unity = number[-1:] # Selects the last number
ten = number[-2:-1] # Selects the penultimate number
hundred = number[-3:-2] # Selects the second number
thousand = number[-4:-3] # Selects the first name
print(f'Unity: {unity}')
print(f'Ten: {ten}')
print(f'Hundred: {hundred}')
print(f'Thousand: {thousand}')
