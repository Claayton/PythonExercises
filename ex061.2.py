# Ex061.2
"""Redo challenge 061, reading the first term and the ratio of an PA
Showing the first 10 terms of the progression using the while function"""

cont = 0
pa = 0
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
print('TheEnd')
print(f'\033[7:40m{"="}\033[m' * 40)
