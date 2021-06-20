# Ex078
valores = []
for p, num in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))

print('-'*40)
print('Você digitou os valores: ', end='\033[32m')
for v in valores:
    print(v, end=' \033[32m')
maior = max(valores)
menor = min(valores)
print(f'\n\033[mO maior valor digitado foi {maior}, na(s) posição(ões): \033[32m', end=' ')
for c, m in enumerate(valores):
    if m == maior:
        print(c, end=' \033[32m')
print(f'\n\033[mO menor valor digitado foi {menor}, na(s) posição(ões) :\033[32m', end=' \033[32m')
for c, m in enumerate(valores):
    if m == menor:
        print(c, end=' \033[32m')
print()
