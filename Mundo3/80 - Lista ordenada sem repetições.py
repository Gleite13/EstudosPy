#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
#   uma lista, já na posição correta de inserção (sem usar o sort()).
#   No final, mostre a lista ordenada na tela


# REFAZER

lista = []

for c in range(0,5):
    n = int((input('Digite um valor: ')))
    if c == 0 or n > lista[-1]: # SE N FOR MAIOR QUE O ULTIMO ELEMENTO, ADICIONA AO FINAL DA LISTA
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista): # enquanto a posição for menor que o len de lista
            if n <= lista[pos]: # se o numero é menor ou igual a lista na posição pos
                lista.insert(pos, n) # na posição pós o inserir o valor N
                break
            pos += 1
print(lista)
