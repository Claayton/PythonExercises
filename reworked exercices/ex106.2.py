# Ex106.2
"""Make a mini-system that uses Python's interactive help.
The user will type the command and the manual will appear.
When the user enters the word 'END', the program will terminate.
NOTE: Use colors."""


def pyhelp():
    function = None
    while True:
        print(f'\033[7:40m{"="}' * 90)
        print(f'{"PyHelp Help System":^90}')
        print(f'{"="}' * 90)
        function = str(input('\033[mFuntion or library: '))
        if function.upper() == 'END':
            print(f'\033[7:41m{"End of the program, thanks for using!":^90}')
            break
        print(f'\033[7:45m{help(function)}\033[m')

pyhelp()