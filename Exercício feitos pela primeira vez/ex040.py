#Exercício040
nota1 = float(input('\033[36mDigite sua nota em portugues: \033[m'))
nota2 = float(input('\033[36mDigite sua nota em matematica: \033[m'))
media = (nota1 + nota2)/2
if media < 5.0:
  print('\033[31mREPROVADO\nSua média foi {:.1f}\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
  print('\033[33mRECUPERAÇÃO\nSua média foi {:.1f}\033[m'.format(media))
else:
  print('\033[32m=-=-=-PARABÉNS-=-=-=\033[m')
  print('\033[32m=-=-=-APROVADO-=-=-=\nSua média foi {:.1f}\033[m'.format(media))
print('\033[36mxD\033[m')
