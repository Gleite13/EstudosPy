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