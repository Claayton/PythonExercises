#Ex019.2
"""A teacher wants to raffle one of his four students to erase the board, make a program that helps him,
by reading their name and writing the chosen name"""

from random import choice
name1 = str(input('What is the name of the first student?: '))
name2 = str(input('What is the name of the second student?: '))
name3 = str(input('What is the name of the third student?: '))
name4 = str(input('What is the name of the fourth student?: '))
list = [name1, name2, name3, name4]
choice = choice(list)
print(f'The choicen student was {choice}')
