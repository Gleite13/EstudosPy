#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

a = [[], [], []]
b = [[], [], []]
c = [[], [], []]
valor = []
for pos in range(0, 2):
    valor.append(int(input('Digite um valor')))
