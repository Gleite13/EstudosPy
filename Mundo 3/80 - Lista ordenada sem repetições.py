#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
#   uma lista, já na posição correta de inserção (sem usar o sort()).
#   No final, mostre a lista ordenada na tela

lista = []
for c in range(0,5):
    c = int((input('Digite um valor: ')))
    lista.append(c)
print(lista)