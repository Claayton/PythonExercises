# Ex098.2
"""Make a program that has a function called counter(), which takes three parameters: Start, End and Step.
Your program has to performer three counts through the created function:
A - From 1 to 10, from 1 to 1;
B - From 10 to 0, every 2;
C - A personalized count."""

from time import sleep


def count(personality=False, start=1, end=10, step=1):
    if personality:
        while True:
            start = int(input('\033[32mStart: \033[m'))
            end = int(input('\033[32mEnd: \033[m'))
            step = int(input('\033[32mStep: \033[m'))
            if step == 0:
                print('\033[31mIt is impossible to perform this count!, try again\033[m')
            else:
                break
    print('\033[35m<>\033[m' * 25)
    print(f"\033[34mCounting from \033[35m{start}\033[34m to \033[35m{end}\033[34m in \033[35m{step}:\033[m")
    if step < 0:
        step = step * -1
    if start < end:
        for c in range(start, end + 1, step):
            print(c, end='\033[31m > \033[m', flush=True)
            sleep(0.5)
        print('Fim!')
    elif start > end:
        for c in range(start, end - 1, -step):
            print(c, end='\033[31m > \033[m', flush=True)
            sleep(0.5)
        print('Fim!')
    print('\033[35m<>\033[m' * 25)


count(start=1, end=10, step=1)
count(start=10, end=0, step=2)
count(personality=True)
print('xD')
