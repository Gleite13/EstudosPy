#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista =[]
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(lista)
lista.sort(reverse=True)
print(lista)
print(len(lista))


if 5 in lista:
    print('O número 5 esta na lista')
else:
    print('não possui numero 5 na lista')