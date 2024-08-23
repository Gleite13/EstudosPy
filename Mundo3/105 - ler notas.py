"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
 e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""

def notas(*media, sit=False):
    """

    :param media:
    :param sit:
    :return: Dicionario com varias informações da turma
    """
    informacoes = {}
    informacoes['maior'] = max(media)
    informacoes['menor'] = min(media)
    informacoes['quantidade'] = len(media)
    informacoes['media'] = sum(media)/len(media)

    if sit:
        if informacoes['media'] >= 7:
            informacoes['situacao'] = 'Boa'
        elif informacoes['media'] >= 5:
            informacoes['situacao'] = 'Razoavel'
        else:
            informacoes['situacao'] = 'Ruim'

    return informacoes


resp = notas(5.5, 2.5, 3.3, sit=True)
print(resp)