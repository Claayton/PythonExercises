colors = [
    '\033[m', # 0 - Limpa
    '\033[31m', # 1 - Vermalho
    '\033[32m', # 2 - Verde
    '\033[33m', # 3 - Amarelo
    '\033[34m', # 4 - Ciano
    '\033[35m', # 5 - Rosa
    '\033[7;35m', # 6 - Rosa Linha
    '\033[7;34m' # 7 - Verde Linha
]

def paint(color=0):
    return colors[color]


def readint(message):
    header(' ', paint(6))
    while True:
        number = str(input(message))
        if number.isnumeric():
            number = int(number)
            header(' ')
            break
        else:
            print(f'{paint(1)}INVALID COMMAND, PLEASE ENTER A VALID NUMBER{paint()}')
    return number


def header(message, color=paint(1)):
    print(f'{color}{message:^40}{paint()}')

def menu():
    from time import sleep
    while True:
        header('MAIN MENU', paint(6))
        print(f"{f'{paint(6)}[ 1 ]':<5}{paint()}{f'{paint(7)} See registered people':<37}{f'{paint(6)}     ':<5}{paint()}")
        print(f"{f'{paint(6)}[ 2 ]':<5}{paint()}{f'{paint(7)} Register new people':<37}{f'{paint(6)}     ':<5}{paint()}")
        print(f"{f'{paint(6)}[ 3 ]':<5}{paint()}{f'{paint(7)} Logout':<37}{f'{paint(6)}     ':<5}{paint()}")
        choice = readint(f'{paint(5)}Your choice: {paint()}')
        if choice == 1:
            header('OPTION 1', paint(5))
            sleep(1)
        elif choice == 2:
            header('OPTION 2', paint(5))
            sleep(1)
        elif choice == 3:
            header('THANKS FOR USING! BYE!', paint(2))
            break
        else:
            header(f'{paint(1)}ERROR, ENTER A VALID OPTION!', paint(1))
            sleep(0.5)
