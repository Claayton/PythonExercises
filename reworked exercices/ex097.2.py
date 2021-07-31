# Ex097.2
"""Make a program taht has a function called write(), which takes any text as a parameter and displays a message with adatable size."""

def write(message):
    size = len(message) + 4
    print('\033[35m=\033[m' * size)
    print(f'\033[34m  {message}\033[m')
    print('\033[35m=\033[m' * size)

write('Curso em Vídeo')
write('Clayton Garcia da Silva')
write('You are staking me right Jaguara hahaha')