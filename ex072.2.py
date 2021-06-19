# Ex072.2
"""Create a program that has a fully populated tuple with a count in full, from zero to twenty
Your program should read a number from the keyboard (between 0 and 20) and display it in full."""

number_in_full = ('Zero', 'One', 'Two', 'Three', 'Four',
                  'Five', 'Six', 'Seven', 'Eight', 'Nine',
                  'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                  'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')

while True:
    number = int(input('\033[34mType a number between 0 and 20: \033[m'))
    if number < 0 or number > 20:
        print('\033[31mINVALID OPTION! \033[m\n\033[34mPlease\033[m', end=' ')
        continue
    else:
        break
print(f'\033[34mYou type the number \033[32m{number_in_full[number]}\033[34m.\033[m')
print('\033[34mxD\033[m')
