# Ex113.2
"""Rewrite the readint() funciton we did in challenge 104, now including the possibility of typing a number of a valid type.
Enjoy and also create a readfloat() function with the same functionality."""

def readint(message):
    while True:
        try:
            value = int(input(message))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mError, please enter a valid integer!\033[m')
            continue
        else:
            break
    return value
           
    


def readfloat(message):
    while True:
        try:
            value = float(input(message))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mError, please enter a valid real number!\033[m')
            continue
        else:
            break
    return value       

print(f'\033[7:40m{"="}\033[m' * 40)
integer = readint('\033[32mEnter an interger: \033[m')
print(f'\033[7:40m{"="}\033[m' * 40)
floater = readfloat('\033[32mEnter a real number: \033[m')
print(f'\033[7:40m{"="}\033[m' * 40)
print(f'\033[34mThe integer value entered was \033[32m{integer}\033[34m and the real value was \033[32m{floater}\033[34m!\033[m')
print(f'\033[7:40m{"="}\033[m' * 40)
print('xD')


# Não esta terminado, bugado!!!