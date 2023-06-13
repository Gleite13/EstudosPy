#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
#   uma lista, já na posição correta de inserção (sem usar o sort()).
#   No final, mostre a lista ordenada na tela


# REFAZER

lista = []
maior = 0
menor = 999
for c in range(0,5):
    c = int((input('Digite um valor: ')))
    if c == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
            lista.insert(c, maior)
            if maior > c:
                lista.remove(maior)

        if c < menor:
            menor = c
            lista.insert(c, menor)
            if menor < c:
                lista.remove(menor)
    #lista.append(c)
print(lista)
print(maior)
print(menor)