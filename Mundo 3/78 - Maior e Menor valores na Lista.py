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


##############

listanum = []
mai = 0
men = 0
for n in range(0, 5):
    listanum.append(int(input('Digite um numero: ')))
    if n == 0:
        mai = men = listanum[n]
    else:
        if listanum[n] > mai:
            mai = listanum[n]
        if listanum[n] > men:
            men = listanum[n]
print(f'Você digitou os valores {listanum}')
print(f'O maior número foi {mai} ')
print(f'O menor número foi {men}')

