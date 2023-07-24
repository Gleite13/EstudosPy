# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogadores = {}
jogadores['jogador1'] = randint(1,7)
jogadores['jogador2'] = randint(1,7)
jogadores['jogador3'] = randint(1,7)
jogadores['jogador4'] = randint(1,7)
for k, v, in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)

