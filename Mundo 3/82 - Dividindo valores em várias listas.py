# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(lista)
print(par)
print(impar)


###############################

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    res = str(input('Deseja continuar? [S/N]: '))
    while res in 'Nn':
        break
for i, v in enumerate(num): #indice e valor
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)