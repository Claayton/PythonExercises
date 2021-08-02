# Ex113.2
"""Rewrite the readint() funciton we did in challenge 104, now including the possibility of typing a number of a valid type.
Enjoy and also create a readfloat() function with the same functionality."""

def readint(message):
    while True:
        try:
            value = int(input(message))
        except (ValueError, TypeError):
            print('\033[31mError, please enter a valid integer!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return value
           
    


def readfloat(message):
    while True:
        try:
            value = float(message)
        except (ValueError, TypeError):
            print('\033[31mError, please enter a valid real number!\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return value

print(f'\033[7:40m{"="}\033[m' * 25)
integer = readint('Enter an interger: ')
floater = readfloat('Enter a real number: ')
print(f'\033[7:40m{"="}\033[m' * 25)
print('xD')


# Não esta terminado, bugado!!!