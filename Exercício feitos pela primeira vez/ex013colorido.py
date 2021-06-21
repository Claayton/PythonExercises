#Ex013b
salario = float(input('\033[34mQual seu salário? \033[m'))
print('\033[33;2m=-\033[m'*20)
print('\033[34mPARABÉNS VOCÊ É O FUNCIONÁRIO DO MÊS\nACABA DE GANHAR UM AUMENTO DE \033[m\033[31m15%\033[m')
print('\033[33m=-\033[m'*20)
print('\033[34mSeu novo salário será \033[m\033[31mR$ {:.2f}\033[m'.format(salario + (salario*15/100)))
print('\033[34mxD\033[m')
