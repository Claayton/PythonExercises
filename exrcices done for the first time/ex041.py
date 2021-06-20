#Exercício041
from datetime import date
year = int(input('\033[32mQual o ano de nascimento do atleta?: \033[m'))
thisyear = date.today().year
idade = thisyear - year
print('\033[32mO atleta se encaixa na categoria: \033[m')
if idade < 0:
    print('\033[31mEssa pessoa nem nasceu ainda seu tongo\033[m')
if idade <= 9:
    print('\033[32mMIRIM\033[m')
elif idade <= 14:
    print('\033[32mINFANTIL\033[m')
elif idade <= 19:
    print('\033[32mJUNIOR\033[m')
elif idade <= 25:
    print('\033[32mSENIOR\033[m')
else:
    print('\033[32mMASTER\033[m')
print('\033[32mxD\033[m')
