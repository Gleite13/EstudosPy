print('\033[0;30;41mOlá Mundo!\033[m')
print('\033[4;33;44mOlá Mundo!\033[m')
print('\033[1;35;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')

a = 2
b = 4
print('Os valores são \033[32m{}\033[m e \033[30;42m{}\033[m!!!' .format(a, b))

nome = 'Guilherme'
print('Olá! Muito prazer em te conhecer, {}{}{}!!' .format('\033[30;42m', nome, '\033[m' ))

nome1 = 'Leite'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!' .format(cores['pretoebranco'], nome1, cores['limpa']))

