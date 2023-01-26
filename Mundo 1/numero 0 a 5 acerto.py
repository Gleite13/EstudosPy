import random
n = random.randint(0,5)
x = int(input('Digite um numero de 0 a 5 para iniciar o jogo: '))
if x==n:
    print('Parabens, voce acertou')
else:
    print('Você errou, mais sorte na proxima')
print('Maquina: {}' .format(n))
print('Humano: {}' .format(x))