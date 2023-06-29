#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
pesados = []
leves = []
c = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    if peso >= 100:
        pesados.append(nome)
        maior = peso
    elif peso <= 70:
        leves.append(nome)
        menor = peso
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
dados.clear()
lista.append(dados[:])
print(f'Foram Cadastrados {len(lista)} Pessoas')
print(f'Os maior peso foi cadastrado foi de {maior}, ácima de 100Kg cadastrados foram: {pesados}')
print(f'O menor peso cadastrado foi de {menor}, abaixo de 70Kg cadastrados foram: {leves} ')


######################################################

temp = []
princ =[]
mai = men = 0
while True
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0
        maior = menor = temp[1] # irá guardar temp na posição 1 que é o peso
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    res = str(input('Quer Conitnuar? [S/N]'))
    if resp in 'Nn'
        break
print(f'Ao todo você cadastrou {len(princ)}')
print(f'O Maior peso doi de {mai}Kg. peso de', end='')
for p in princ: # Para cada pessoa dentro da lista princ
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O Menor peso foi de {men}Kg. peso de ', end='')
for p in princ :
    if p[1] == men:
        print(f'{p[0]}', end='')

