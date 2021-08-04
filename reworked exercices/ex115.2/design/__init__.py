colors = [
    '\033[m',       # 0 - Limpa
    '\033[31m',     # 1 - Vermalho
    '\033[32m',     # 2 - Verde
    '\033[33m',     # 3 - Amarelo
    '\033[34m',     # 4 - Ciano
    '\033[35m',     # 5 - Rosa
    '\033[7;35m',   # 6 - Rosa Linha
    '\033[7;32m',   # 7 - Verde Linha
    '\033[7;31m',   # 8 - Vermelho Linha
    '\033[7;34m'    # 9 = Ciano Linha
]

def paint(color=0):
    return colors[color]


def header(message, color=paint(1)):
    print(f'{color}{message:^40}{paint()}')

def menu():
    from time import sleep
    import data
    while True:
        header('MAIN MENU', paint(6))
        print(f"{f'{paint(6)}[ 1 ]':<5}{paint()}{f'{paint(7)} See registered people':<37}{f'{paint(6)}[ 1 ]':<5}{paint()}")
        print(f"{f'{paint(6)}[ 2 ]':<5}{paint()}{f'{paint(7)} Register new people':<37}{f'{paint(6)}[ 2 ]':<5}{paint()}")
        print(f"{f'{paint(6)}[ 3 ]':<5}{paint()}{f'{paint(7)} Logout':<37}{f'{paint(6)}[ 3 ]':<5}{paint()}")
        header(' ', paint(6))
        choice = data.readint(f'{paint(5)}Your choice: {paint()}')
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 3:
            return 3
        else:
            header(f'ERROR, ENTER A VALID OPTION!', paint(8))
            sleep(0.7)
