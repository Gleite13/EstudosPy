#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

nope = []
lista = []
pesados = []
leves = []
while True:
    nope.append(str(input('Digite seu nome: ')))
    nope.append(float(input('Qual o seu peso: ')))

    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break

lista.append(nope[:])
print(nope)
print(lista)
for p in lista:
    if p[p+1] >= 100:
        print(p[1])