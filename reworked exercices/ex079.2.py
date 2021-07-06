# Ex079.2
"""Create a program where the user can type several numerical values and enter them in a list.
If the number alrealy exists in there, it will not be added. At the end, all the numerical values entered will be displayed, in ascending order"""

list = []
again = ''

while again != 'n'.lower():
    value = int(input('\033[32mEnter a value: \033[m'))
    if value not in list:
        list.append(value)
        print('\033[32mSuccessfuly added value!\033[m')
    else:
        print('\033[34mDuplicate values will not be added!\033[m')
    while True:
        again = str(input('Do you want to continue?: \033[32m[S | N]\033[m: '))
        if again != 'n'.lower() and again != 's'.lower():
            print('\033[31mPlease, type "S" to continue, and "N" to exit!\033[m' )
        else: 
            break
print(f'You entered the values: {sorted(list)}')
print('\033[32mxD\033[m')
