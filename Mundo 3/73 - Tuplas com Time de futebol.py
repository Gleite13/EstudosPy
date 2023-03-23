# Criar um Tupla com os 20 primeiros colocados do campeonato brasileiro de futebol em ordem de colocação
# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Grêmio.

times = ('Flamengo', 'Palmeiras', 'Athletico Paranaense', 'Atlético Mineiro',
         'São Paulo', 'Fluminense', 'Fortaleza', 'Corinthias', 'Santos',
         'Internacional', 'Grêmio', 'América Mineiro', 'Atlético Goianiense',
         'Ceará', 'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Cruzeiro',
         'Goiás', 'Cuiabá')
while True:
    print('-=-' * 15)
    print('Painel do Brasileirão'.center(40))
    print('-=-' * 15)
    print('[1]Os 5 primeiros Colocados\n'
          '[2]Os 4 ultimos colocados\n'
          '[3]Times em ordem alfabética\n'
          '[4]Em que posição o Grêmio esta?\n'
          '[5]Para sair')
    n = int(input('Qual opção desejada?'))
    if n == 1:
        print('Os primeiros times 5 times do Campeonato Brasileiro São:')
        print(times[0:5])
    if n == 2:
        print('Os 4 Ultimos do Campeonato Brasileiro São:')
        print(times[16:])
    if n == 3:
        print('Times em Ordem Alfabética:')
        print(sorted(times))
    if n == 4:
        print(f'O Grêmio esta na {times.index("Grêmio")+1}° Posição')
    if n == 5:
        print('Obrigado por participar')
        break




