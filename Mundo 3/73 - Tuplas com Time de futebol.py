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
    print('-=-' * 30)
    print('Painel do Brasileirão')
    print('-=-' * 30)
    print('Os primeiros times 5 times do Campeonato Brasileiro São:')
    print(times[0:5])
    print('Os 4 Ultimos do Campeonato Brasileiro São:')
    print(times[16:])
    print('Times em Ordem Alfabética:')
    print(sorted(times))
    print(f'O Grêmio esta na {times.index("Grêmio")+1}° Posição')




