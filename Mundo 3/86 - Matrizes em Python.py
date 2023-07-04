#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

a = [[], [], []]
b = [[], [], []]
c = [[], [], []]
valor = []
for pos in range(0, 9):
    valor.append(int(input('Digite um valor para ')))
a[0].append(valor[0])
a[1].append(valor[1])
a[2].append(valor[2])
b[0].append(valor[3])
b[1].append(valor[4])
b[2].append(valor[5])
c[0].append(valor[6])
c[1].append(valor[7])
c[2].append(valor[8])
valor.clear()
print(f'[ {a[0][0]} ] [ {a[1][0]} ] [ {a[2][0]} ]')
print(f'[ {b[0][0]} ] [ {b[1][0]} ] [ {b[2][0]} ]')
print(f'[ {c[0][0]} ] [ {c[1][0]} ] [ {c[2][0]} ]')


#######################################################

matriz = [[0,0,0],[0,0,0],[0,0,0]] # Entrada
for l in range(0, 3): # L de Linha
    for c in range(0, 3): # C de coluna
        matriz[l][c] = int(input(f'Digite um valor para {l} e {c}: ')) # matriz na linha L e na coluna C
for l in range(0, 3): # Saída
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
    print()