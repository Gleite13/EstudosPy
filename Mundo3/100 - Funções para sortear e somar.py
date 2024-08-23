#Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

lista = []
def sorteia():
    for c in range(0,5):
        lista.append(randint(0, 9))
    print('Sorteando 5 valores na lista: ',end='')
    for c in lista:
        print(c, end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar():
    cont = 0
    for c in lista:
        if c % 2 == 0:
            cont += c
    print(f'Somando os valores pares de {lista}, temos {cont}')


print(sorteia())
print(somaPar())

# ASSISTIR RESOLUÇÂO DO EXERCICIO!!!!