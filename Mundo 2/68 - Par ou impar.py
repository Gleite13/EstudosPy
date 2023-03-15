# Jogo de Par ou Ímpar

v = 0
from random import randint
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor: '))
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]  ')).strip().upper()[0]
    print(f'Você Jogou {jogador} e o Computador {computador} o total é: {soma} ' ,end='')
    print('deu PAR' if soma % 2 == 0 else 'deu Impar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você Venceu')
            v += 1
        else:
            print('Você Perdeu')
            break
print(f'Você venceu {v} vezes')
