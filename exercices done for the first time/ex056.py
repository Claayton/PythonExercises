#Exercício056
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
mulher20 = 0
for c in range(1, 4 + 1):
  name = str(input('Qual o nome da {}° pessoa?: '.format(c))).capitalize()
  age = int(input('Qual a idade da {}° pessoa?: '.format(c)))
  sex = str(input('Qual o sexo da {}° pessoa? [M ou F]: '.format(c))).upper()
  somaidade += age
  if c == 1 and sex in 'Mm':
    maioridadehomem = age
    nomemaisvelho = name
  if sex in 'Mm' and age > maioridadehomem:
      maioridadehomem = age
      nomemaisvelho = name
  if sex == 'F' and age < 20:
    mulher20 += 1
media = somaidade / 4
print('A média de idade dessas pessoas é {:.0f}'.format(media))
print('O nome do homem mais velho é {}'.format(nomemaisvelho))
print('{} mulheres tem menos de 20 anos'.format(mulher20))
print('xD')
