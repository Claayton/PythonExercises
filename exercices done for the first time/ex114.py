# Ex114
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acesível no momento!')
else:
    print('Conseguimos acessar o site pudim com sucesso!')
