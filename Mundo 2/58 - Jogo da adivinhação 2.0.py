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
