from funçoes import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    from time import sleep
    try:
        a = open(nome, 'rt')
    except:
        cabeçalho('Erro ao ler arquivo!', pinta(5))
    else:
        cabeçalho('Pessoas Cadastradas', pinta(3))
        sleep(1)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:_<30}{dado[1]:_>5} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='defaut', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'{pinta(2)}Novo registro de {nome} adicionado!{pinta()}')
            a.close()
