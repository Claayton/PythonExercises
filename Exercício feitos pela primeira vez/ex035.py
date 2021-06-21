#Exercício035
print('DIGITE UM VALOR PARA TRÊS SUPOSTAS RETAS\nE TE MOSTRAREI SE É POSSÍVEL FORMAR UM TRIÂNGULO')
AB = float(input('Digite o tamanho da primeira reta: '))
CD = float(input('Digite o tamanho da segunda reta: '))
EF = float(input('Digite o tamanho da terceira reta '))
lista = [AB, CD, EF]
lista = (sorted(lista))#organiza lista em ordem crescente
listaordem = lista[0]+lista[1]#soma os dois valores <
if listaordem > lista[2]:#se a soma do dois < forem > que o terceiro valor é possivel formar um triângulo
  lista = ('SIM! é possim formar um triângulo')
else:
  lista = ('NÃO! impossível formar um triângulo')
print(lista)
print('xD')
