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


from random import randint
from time import sleep
lista2 = []
jogos = []
print('-' * 30)
print('    JOGA NA MEGA SENA    ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
cont = 0
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista: # faz que adicione a lista numeros nao repetidos
            lista.append(num)
            cont += 1
        if cont >= 1:
            break
    lista2.sort()
    jogos.append(lista2[:])
    lista2.clear
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)