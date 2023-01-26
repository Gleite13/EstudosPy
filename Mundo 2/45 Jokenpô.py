from random import randint
lista = ['Pedra','Papel','Tesoura']
computador = randint(0,2)
print('''Suas Opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 20)
print('Computador jogou {}' .format(lista[computador]))
print('Jogador Jogou {}' .format(lista[jogador]))
print('-=' * 20)
if computador == 0: #PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Opção Invalida')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Opção Invalida')

elif computador == 2:  #TESOURA
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção Invalida')

else:
    print('Opção Invalida')