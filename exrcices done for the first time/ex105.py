# Ex105
def notas(*nota, sit=False):
    """
    => Calcula vários dados sobre as notas registradas de um aluno.
    :param nota: Notas registradas de um aluno.
    :param sit: (Opcional) Mostra a situação do aluno de acordo com a média obtida.
    :return: Um dicionário com todos os dados retirados de acordo com as notas registradas.
    """
    dados = {}
    total = cont = maior = menor = 0
    dados['Qtdade_de_notas'] = len(nota)
    dados['Maior_nota'] = max(nota)
    dados['Menor_nota'] = min(nota)
    media = sum(nota)/len(nota)
    dados['Média'] = media
    if sit:
        if media <= 6:
            dados['Situação'] = 'Ruim'
        elif 5 < media < 7:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Boa'
    return dados


notas_dos_alunos = notas(5.5, 9.5, 10, 6.5, sit=True)
print(notas_dos_alunos)
help(notas)
