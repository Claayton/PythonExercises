#Exercíco049
num = int(input('\033[31mDigite um número: '))
print('\033[31m='*20)
print('\033[33m-=-=-=TABUADA=-=-=-')
print('\033[31m='*20)
for c in range(1, 10 + 1): #indica a repetição de 1 ate 10
    print('\033[36m{}  x {:>2} = \033[32m{:>2}\033[m'.format(num, c, c * num))
print('\033[31m='*20)
print('\033[31mxD\033[m')
