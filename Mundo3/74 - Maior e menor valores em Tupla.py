# Criar um programa que leia 5 números aleátorios e colocar em uma tupla
# Mostrar a listagem dos numeros gerados
# Indicar maior e menor da lista

from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0,10))
organizado = sorted(tupla)
print(tupla)
print(f'O maior número é {organizado[4]}')
print(f'O menor número é {organizado[0]}')
