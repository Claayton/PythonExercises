#Ex004b
algo = (input('\033[34m''Digite algo: ''\033[m'))
print('São letras ou palavras?: \033[33m{}\033[m'.format(algo.isalpha()))
print('Está em maiúsculo?: \033[34m{}\033[m'.format(algo.isupper()))
print('Está em minúsculo?: \033[35m{}\033[m'.format(algo.islower()))
print('Está captalizada?: \033[36m{}\033[m'.format(algo.istitle()))
print('Só tem espaço?: \033[31m{}\033[m'.format(algo.isspace()))
print('É numérico?: \033[32m{}\033[m'.format(algo.isnumeric()))
print('xD')
