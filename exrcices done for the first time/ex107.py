# Ex107 - Programa
import moeda

preço = float(input('Digite o preço: '))
print(f'A metade de {preço} é {moeda.metade(preço)}.')
print(f'O dobro de {preço} é {moeda.dobro(preço)}.')
print(f'Aumentando 10% de {preço}, temos {moeda.aumentar(preço, 10)}.')
print(f'Reduzindo 13% de {preço}, temos {moeda.diminuir(preço, 13)}')
