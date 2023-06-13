#LISTAS SÃO MUTAVEIS!
#Listas sao feitas por []

num = [2,5,9,1]
num[2] = 3 # ira trocar a posição 2 da lista pelo valor 3

num.append(7) #Adiciona a lista o valor 7
num.insert(2, 0) # Irá inserir na posição 2 o valor 0

if 4 in num: # caso precise remover algo que nao esteja na lista e nao ocorrer erro caso nao exista na mesma
    num.remove(4)
else:
    print('Não achei o numero 4')

#####

valores = []
valores.append(5) # adiciona valor 5 a lista
valores.append(9)
valores.append(4)

valores.insert(0,'pizza')# irá inserir pizza na pozição zero

for v in valores: #formas de visualizar os valores
    print(f'{v}...', end='')


for c, v in enumerate(valores): #visualizar valores com o numero das chaves
    print(f'Na posição {c} encontrei o valor{v}...', end='')
print('Cheguei ao final da lista')

for cont in range(0, 5): #formas de inserir valores solicitando ao usuário
    valores.append(int(input('Digite um valor')))

###

a = [2, 3, 4, 7]
b = a[:] #para o Python Fazer uma Copia de A, necessário usar [:] caso nao seja veito ele irar ligar uma lista na outra
b[2] = 8 #subustitui a copia B na posição 2 para 8

print(f'Lista A: {a}')
print(f'Lista A: {b}')


print(num)
print(f'Essa lista tem {len(num)} elementos')


#Deletar

del lista[3] # delete o objeto da lista na posição 3

lista.pop(3) #Normalmente elimina o ultimo elemente, porem é possivel selecionar a posição no caso com o (3)

lanche.remove('NOME do objeto') # REMOVE PELO NOME DO OBJETO

if 'pizza' in lanche # serve para remover caso haja o valor pizza dentro do valor lanche
    lanche.remove('pizza')

#CRIAR

valores=list(range(4,11)) #Inicia  uma lista dentro de valores de 4 ate 10
#EX
# 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6

valores=[8,2,5,5,9,3,0]
velores.sort() #Coloca a lista em forma ordenada crescente

valores.sort(reverse=True) # Coloca a lista de forma ordenada decrescente

len(valores) #verifica quantos valores existem da lista que inicia de 0

