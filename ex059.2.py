# Ex059.2
"""Create a program that reads two values and show the folowing menu:
[1] Add
[2] Multiply
[3] Bigger
[4] Nem numbers
[5] Exit the program
Your program should perform the requested operation in each case."""

choice = 0
first_number = int(input('First number: '))
second_number = int(input('Second number: '))
while choice != 5:
    print("""    [1] Add
    [2] Multiply
    [3] Bigger
    [4] New numbers
    [5] Exit the program""")
    print('-'*30)
    choice = int(input('What is your choice?: '))
    if choice == 1:
        add = first_number + second_number
        print(f'The sum of this number is \033[32m{add}\033[m')
    elif choice == 2:
        multiply = first_number * second_number
        print(f'The multiply of this numbers is \033[32m{multiply}\033[m')
    elif choice == 3:
        bigger = first_number
        if second_number > first_number:
            bigger = second_number
        print(f'The bigger between this numbers is \033[32m{bigger}\033[m')
    elif choice == 4:
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
    elif choice == 5:
        print('\033[32mThanks for using the program!\033[m')
    else:
        print('\033[31mINVALID COMMAND!, TRY AGAIN\033[m')
