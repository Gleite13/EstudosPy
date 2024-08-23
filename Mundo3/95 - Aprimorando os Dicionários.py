#Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
partidas = list()
lista = []
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    tota = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, tota):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    resp = str(input('Deseja continuar? [S/N]:'))
    if resp in 'Nn':
        break
print('-=' * 30)
print('COD    NOME    GOLS          TOTAL')
print('-' * 30)
for k, v in enumerate(lista):
    print(f'{k:>}    {v["nome"]}    {v["gols"]}          {v["total"]}')
print('-' * 30)
while True:
    p = int(input('Mostrar dados de qual jogador? (999 para interromper) '))
    if p == 999:
        break
    elif p == len(lista):
        print('erro')



print(partidas)
print(jogador)
print(lista)
#print('-=' * 30)
#print(jogador)
#print('-=' * 30)
#for k, v in jogador.items():
#    print(f'O campo {k} tem o valor {v}')
#print('-=' * 30)
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
#print(f'Foi um total de {jogador["total"]} gols')

####################################################

time = []
jogador = dict()
partidas = list()
while True:
    jogador.clear
    jogador['nome'] = str(input('Nome do Jogador: '))
    tota = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tota):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
for i in jogador.keys():# Cabeçalho
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:>4}', end='') # numero do jogador
    for d in v.values(): # para cada dado em d do valor em v
        print(f'{str(d):<15}', end='')# Uma STR do dado
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'Erro! não existe jogador com o código {busca} ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')# ira buscar em time na posição selecionado por busca escolhendo a nome dentro da lista
        for i, g in enumerate(time[busca]["gols"])
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< Volte Sempre >>')