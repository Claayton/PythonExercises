# Ex083
expressao = []
resultado = ''
exp = str(input('Digite uma expressão: '))
for c in exp:
    if c == '(':
      expressao.append('(')
    elif c == ')' and len(expressao) > 0:
      expressao.pop()
    elif c == ')' and len(expressao) == 0:
      resultado = '\033[31mERRADA\033[m'
if len(expressao) == 0:
  resultado = '\033[32mCORRETA\033[m'
else:
  resultado = '\033[31mERRADA\033[m'
print(f'\033[32mSua expressão está {resultado}\033[m')
