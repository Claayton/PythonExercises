# Ex 076
print(f'\033[1;41m{"LISTAGEM DE PREÇOS":^60}\033[m')
listagem = ('Lapis', 1.75,'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'transferidor', 4.20,'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
cont = 0
for lista in listagem:
  if cont % 2 == 0:
    print(f"{lista:.<51}{'R$':<3}", end='')
    cont += 1
  else:
    print(f"{lista:>6.2f}")
    cont += 1
print(f'\033[1;41m{" ":^60}\033[m')