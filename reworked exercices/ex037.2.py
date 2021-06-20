# Ex037.2
"""Write a program that reads any integer and ask the user to choose the conversion base:
1 for binary
2 for octal
3 hexadecimal"""

number = int(input('\033[32mtype an integer: \033[m'))
print('\033[35m[1] for binary\n[2] for octal\n[3] for hexadecimal\033[m')
choice = str(input('\033[32mChose your conversion base: \033[m'))
if choice == '1':
    print(f'\033[32m{number} converted in binary is: {bin(number)[2:]}')
elif choice == '2':
    print(f'\033[32m{number} converted in octal is {oct(number)[2:]}')
elif choice == '3':
    print(f'\033[32m{number} converted in hexadecimal is {hex(number)[2:]}')
else:
    print('\033[31mINVALID OPTION, PLEASE TRY AGAIN\033[m')
