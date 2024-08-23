#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0 ]]
somap = terc = maior = 0
for l in range(0, 3): # Entrada da dados
    if maior == matriz[l][0]:
        maior = matriz[l][0]
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para {l} e {c}: ')))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        terc += matriz[l][2]
        if matriz[l][c] > maior:
            maior = matriz[l][c]

for l in range(0, 3): # saida de dados
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma dos valores pares da matriz é de: {somap}')
print(f'O valor da soma da terceira coluna é de: {terc}')
print(f'O maior valor da Matriz é {maior}')


##############################

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l} e {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}')
        if matriz[l][c] % 2 == 0:
            somap = matriz[l][c]
    print()
print(f'A soma dos valores pares é de {somap}')
for l in range(0, 3):
    terc += matriz[l][2]
print(f'A soma dos valores da terceira coluna é de {terc}')
for c in range(0, 3)
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior
        maior = matriz[1][c]
print(f'O Maior valor da segunda linha é {maior}')