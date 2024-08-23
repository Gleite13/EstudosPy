# PYTHON TUPLAS

() Tuplas

[] Listas

{} Dicionarios

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #TUPLA
print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}') #Mostra a no comando for as Tuplas uma de cada vez

for cont in range (0, len(lanche)):#Inicia contagem 0 em lanche utilizando função len(Ler numero de objetos)
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  #Cont irá iniciar contagem do 0

for pos, comida in enumerate(lanche)#Função enumerate enumera o o numero de posiçoes em lanche
    print(f'Eu vou comer {comida} na posição {pos}')#pos ira enumerar a posição da contagem

------------------------------

print(sorted(lanche))#função sorted funciona ordenadamente Alfabeticamente

-----------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Junta as duas tuplas de foram **** (2, 5, 4, 5, 8, 1, 2)
print(c)
c = b + a # Troca as posições dessa forma *** (5, 8, 1, 2, 2, 5, 4)
print(c)

print(len(c)) # Vai dizer quantos elementos possuem em c ** escrevendo 7, pois há 7 numeros guardados

print(c.count(5)) # vai dizer quantas vezes esta aparecendo o número 5 na tupla

print(c.index(8)) # fazendo c = b + a vai mostrar em qual posição aparece o numero 8, que é a posição 1, lembrando 0 ser a primeira posição
# .index serve para a primeira ocorrencia de posição

print(c.index(5, 1)) # conta qual o primeiro numero 5 a partir da posição 1

-----------------------------------------------

#Tuplas no Python podem conter strings e numeros
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)# função del serve para eliminar qualquer coisa em python incluindo as tuplas
print(pessoa)