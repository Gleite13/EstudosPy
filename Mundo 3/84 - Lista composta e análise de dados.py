#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
pesados = []
leves = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    if peso >= 100:
        pesados.append(peso)
    elif peso <= 70:
        leves.append(peso)
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break

lista.append(dados[:])
print(f'Foram Cadastrados {len(lista)} Pessoas')
print(lista)
print(f'{pesados})
print(leves)