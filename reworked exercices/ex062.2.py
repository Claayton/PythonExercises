# Ex062.2
"""Improve challenge 061 by asking the user if he wants to show some more terms.
The program will close when he says he wants to show '0' terms."""

cont = 0
pa = 0
more = 1
print(f'\033[7:40m{"="}\033[m' * 40)
print(f'{"10 TERMS OF A PA":^40}')
print(f'\033[7:40m{"="}\033[m' * 40)
first = int(input('What is the first term of a PA?: '))
ratio = int(input('What is the ratio of a PA?:'))
while cont < 10:
    cont += 1
    if cont == 1:
        pa = first
    print(pa, end=' \033[32m> \033[m')
    pa += ratio
print('Pause')
more = int(input('How many terms you want to see more?: '))
while more > 0:
    while more > 0:
        more -= 1
        print(pa, end=' \033[32m> \033[m')
        pa += ratio
    print('Pause')
    more = int(input('How many terms you want to see more?: '))
print('The End')
print(f'\033[7:40m{"="}\033[m' * 40)
