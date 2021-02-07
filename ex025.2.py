# Ex025.2
"""Create a program that reads the person's name, and says if they have 'SILVA' in their name"""

name = str(input('Enter a name: ')).strip().upper()
print(f'There is "Silva" in that name?: {"SILVA" in name}')
