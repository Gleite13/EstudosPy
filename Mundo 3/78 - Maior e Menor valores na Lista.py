#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
maior = 0
menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite o {c+1}º valor: ')))
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior =  numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
if maior in numeros:
    print(f'O maior número é {maior} e esta na posição: {numeros.index(maior)}')
if menor in numeros:
    print(f'O menor número é {menor} e esta na posição: {numeros.index(menor)}')


