# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#aproveitamento = {}
#gol = []
#total = tot = 0
#aproveitamento['nome'] = str(input('Nome do Jogador: '))
#part = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
#for c in range(0, part):
#    gols = int(input(f'   Quantos gols na partida {c}: '))
#    gol.append(gols)
#    total += gols
#    tot += 1
#aproveitamento['gols'] = gol
#aproveitamento['total'] = total
#print('-=' * 30)
#print(aproveitamento)
#print('-=' * 30)
#for k, v in aproveitamento.items():
#    print(f'O campo {k} tem o valot {v}')
#print('-=' * 30)
#print(f'O jogador {aproveitamento["nome"]} jogou {tot}')
#for c, l in enumerate(gol):
#    print(f'    Na partida {c}, fez {l} gols.')
#print(f'Foi um total de {tot}')

########################################

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tota = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tota):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')

