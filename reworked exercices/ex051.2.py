# Ex051.2
"""Develop a program that reads the first term and the ratio of a PA, at the end,
Show the first 10 terms of this progression"""

print(f'\033[7:40m{"="}\033[m' * 40)
print(f'{"10 TERMS OF A PA":^40}')
print(f'\033[7:40m{"="}\033[m' * 40)
first = int(input('What is the first term of a PA?: '))
ratio = int(input('What is the ratio of a PA?:'))
for pa in range(first, ratio * 10 + 1, ratio):
    print(pa, end=' \033[32m> \033[m')
print('TheEnd')
print(f'\033[7:40m{"="}\033[m' * 40)
