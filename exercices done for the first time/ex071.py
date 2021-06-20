#Exercício071
cinquenta = 0
vinte = 0
dez = 0
um = 0
total = 0
print('\033[36m=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\033[36m>>>>>> BANCO GARCIA <<<<<<<')
print('\033[36m=-=-=-=-=-=-=-=-=-=-=-=-=-=')
saque = int(input('\033[32mQuanto você deseja sacar?: \033[m'))
while True: #Realiza a repetição para somar as cédulas
    if saque < 1: #Interrompe a repetição caso o valor esteja menor que 1 real
        break
    while True: #Realiza a repetição para cédulas de 50 reais
        if saque < 50: #Interrompe a repetição caso o valor esteja menor que 50 reais
            break
        saque -= 50 #Subtrai 50 reais a cada repetição
        cinquenta += 1 #Soma mais uma cédula  de 50 a cada repetição
    while True: #Realiza a repetição para cédulas de 20 reais
        if saque < 20: #interrompe a repatição caso o valor esteja menor que 20 reais
            break
        saque -= 20 #Subtrai 20 reais a cada repetição
        vinte += 1 #Soma mais uma cédula de 20 a cada repetição
    while True: #Realiza a repetição para cédulas de 10 reais
        if saque < 10: #Interrompe a repetição caso o calos esteja menos que 10 reais
            break
        saque -= 10 #Subtrai 10 reis a cada repetição
        dez += 1 #Soma mais uma cédula de 10 reias a cada repetição
    while True: #Realiza a repetição para cédulas de 1 real
        if saque < 1: #Interrompe a repetição caso o vlor esteja menor que 1 real
            break
        saque -= 1 #Subtrai 1 real a cada repetição
        um += 1 #Soma uma cédula de 1 real a cada repetição
total = cinquenta * 50 + vinte * 20 + dez * 10 + um * 1
#Multiplica o número de cédulas pelos seus devidos valores e depois soma para garantir o resultado correto
print(f'\033[32mCédulas de R$: 50.00: \033[m{cinquenta:.0f}')
print(f'\033[32mCédulas de R$: 20.00: \033[m{vinte:.0f}')
print(f'\033[32mCédulas de R$: 10.00: \033[m{dez:.0f}')
print(f'\033[32mCédulas de R$:  1.00: \033[m{um:.0f}')
print(f'\033[32mTotal {total:.>25.2f}')
print('\033[36mObrigado por utilizar o BANCO GARCIA\nTenha um BOM DIA!')
print('\033[36mxD')
