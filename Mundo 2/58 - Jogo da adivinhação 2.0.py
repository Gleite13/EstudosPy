import random
n = random.randint(1, 10)
x = int(input('Digite um numero de 0 a 10 para começar o JOGO: '))
while x != n:
    print('Maquina {} '.format(n))
    print('Você {}' .format(x))
    n = random.randint(1, 10)
    x = int(input('Você errou, Tente outro numero: '))
print('Maquina {} '.format(n))
print('Você {}' .format(x))



######################################################

from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um numero de 0 a 10.')
print('Sera que você consegue advinhar qual foi? ')
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    if jogador == computador
        acertou = True
print('Acertou!')




