# Ex080.2
"""Create a program where the user can type five numerical values, and enter them in a list,
already in the correct insertion position (without using sort()).
At the end show the ordered list on the screen."""

values = []
temp = []

for c in range(0, 5): 
    number = int(input('\033[34mEnter a number: \033[m'))
    if c == 0 or number > values[-1]:
        values.append(number)
        print('\033[32mValue added to \033[33mEND\033[32m of list\033[m')
    elif number < values[0]:
        values.insert(0, number)
        print('\033[32mValue added to  \033[33mBEGINNING\033[32m of list.')
    else:
        for p, n in enumerate(values):
            if number > n:
                temp.append(number)
        values.insert(p, temp[0])
        print(f'\033[32mValue added to \033[33mPOSITION {p}\033[32m of list\033[m.')
        temp.pop()
print(f'\033[34mThe values entered were: \033[33m{values}\033[m.')
print('\033[34mxD\033[m')
