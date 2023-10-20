# Faça um programa que tenha a função chamada contador que receba tres parêmtros: inicio, fim e passo
# e realize a contagem
# Seu programa tem que realizar tres contagens artavens da função criada
# A) de 1 até 10 de 1 em 1
# B) de 10 ate 0 de 2 em 2
# C) uma contagem personalizada
from time import sleep


def texto(txt):
    print('-' * len(txt))
    print(txt)

def contador(a, b, c):
    for c in range(a,b, c):
        print(c, end=' ')
        sleep(0.5)


print(texto('Contador de 1 a 10 pulando de 1 em 1'))
print(contador(1,11, 1))

print(texto('Contador de 10 a 0 pulando de 2 em 2'))
print(contador(10, -2, -2))

print('Agora é sua vez de personalizar!!!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))


if a > b and c > 0: # COMO IDENTIFICAR QUE o numero é positivo?????
    c = (c*-1)
    print(contador(a, b, c))
elif c == 0:
    if a < b:
        c = 1
        print(contador(a, b, c))
    elif a > b:
        c = -1
        print(contador(a, b, c))
else:
    print(contador(a, b, c))


# VISUALIZAR VIDEO