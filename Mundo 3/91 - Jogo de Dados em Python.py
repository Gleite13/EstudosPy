# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter # Utilizado na resolução do exercício original, para pegar o item do dicionario
jogadores = {}
jogadores['jogador1'] = randint(1,7)
jogadores['jogador2'] = randint(1,7)
jogadores['jogador3'] = randint(1,7)
jogadores['jogador4'] = randint(1,7)
for k, v, in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('-=' * 30)
for i in sorted(jogadores, key=jogadores.get, reverse=True ): #função Key=VARIAVEL.get irá pegar todos os valores da chave e ordenalos, irá tratar a função como uma lista
    print(i, jogadores[i])
    sleep(0.5)
print('-=' * 30)
print()
#########################################################

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('OS NÚMEROS SORTEADOS FORAM!')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}') # v[0] e v[1], pois ranking foi tratado como lista
    sleep(0.5)


