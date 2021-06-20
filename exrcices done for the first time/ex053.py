#Exercício053
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper() #Ja tira os espaços e deixa maiusculo
num = len(frase) #Indica quantas letras tem  a frase
for c in range(0, num): #indica a repetição de 0 ate o numero de letras da frase
  certo = (frase[c:c + 1]) #repete cada letra da frase
for c in range(num, 0 - 1, -1): #indica a repetição de tras para a frente
  invertido = (frase[c:c + 1]) #repete cada letra da frase
if certo == invertido:
  print('Esta frase é um palídromo')
else:
  print('Esta frase NÃO é um palídromo')
print('xD')
