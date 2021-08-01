# Ex104.2
"""Create a program that has the readint() function, which will work similarly to Python's input() function, except that it validates to accept only a numeric value.
Ex: n = readint('Enter a number: ')."""

def readint(message):
    print('\033[35m--\033[m' * 25)
    while True:
        number = str(input(message))
        if number.isnumeric():
            number = int(number)
            return number
            break
        else:
            print('\033[31mINVALID COMMAND, PLEASE ENTER A VALID NUMBER\033[m')

number = readint('Enter a number: ')
print(f'\033[32mYou just typed the number \033[35m{number}\033[32m.\033[m')
print('xD')
