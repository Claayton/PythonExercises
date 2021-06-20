#Exercício055
maior = 0
menor = 0
for c in range(1, 5 + 1):
  massa = float(input('Digite o peso da {}° pessoa: '.format(c)))
  if c == 1:
    maior = massa
    menor = massa
  else:
    if massa > maior:
      maior = massa
    if massa < menor:
      menor = massa
print('A pessoa com menor peso tem {} kg'.format(menor))
print('A pessoa com maior peso tem {} kg'.format(maior))
print('xD')
