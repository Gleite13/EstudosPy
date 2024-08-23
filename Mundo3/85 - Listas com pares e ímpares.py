# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
# em ordem crescente.

lista = []
par = []
impar = []
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° numero: '))
    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)
par.sort()
impar.sort()
lista.append(par[:])
lista.append(impar[:])

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')
print(f'Os Valores da lista são {lista}')


#####################################################################


num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c} valor'))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')