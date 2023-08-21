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
    print(f'{k}    {v["nome"]}    {v["gols"]}          {v["total"]}')

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