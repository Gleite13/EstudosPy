#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
temp = []
jogos = int(input('Deseja fazer quantos jogos? '))
for n in range(0, jogos):
    for c in range(0, 6):
        num = randint(0, 60)
        if num not in temp:
            temp.append(num)
        else:
            num = randint(0, 60)
            temp.append(num)
        temp.sort()
    lista.append(temp[:])
    temp.clear()
print('Sorteando Números:')
for c, n in enumerate(lista):
    print(f'Jogo {c+1}: {n} ')
    sleep(0.5)



###########################################################


