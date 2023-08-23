def mostralinha():
    print('-' * 30)

#Programa principal
mostralinha()
print('      SISTEMA DE ALUNOS               ')
mostralinha()
mostralinha()
print('      CADASTRO DE FUNCIONÁRIOS     ')
mostralinha()
mostralinha()
print('      ERRO DE SISTEMA            ')
mostralinha()

#------------------------------------------

def mensagem(msg): # ira imprimir uma linha a funçao dentro de msg e depois outra linha
    print('-' * 30)
    print(msg)
    print('-' * 30)


#Programa Principal
mensagem('Sistema de alunos') # Será copiado direto para o parametro MSG
mensagem('Aprenda Python')
mensagem('Guilherme Leite')

#-----------------------------------------------------

def soma(a, b):
    s =  a + b
    print(s)


#programa principal
soma(4, 5) # Ira mostrar a soma dos numeros indicado em a e b nas posições
soma(8, 9)
soma(2, 1)

def som(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Para especificar posições na função
som(a=4, b=5)
# Ou
som(b=4, a=5)

#-----------------------------------
#CONTADOR // EMPACOTAR PARAMETROS

def contador(*num): # Desempacotar ## o cara vai densempacotar tudo e joga tudo dentro de num
    print(num) # ira criar tuplas


contador(2, 1, 7)  # Irá Criar tuplas
contador(3, 4)
contador(2, 3, 5, 6, 7, 8)

def cont(*num):
    for valor in num # Para valor em num mostre
        print(valor, end='')
    print('FIM')

cont(2, 3 , 5)
cont(5, 1)
cont(2, 5, 7, 9)

def cont(*num):
    tam = len(num) # Ira mostra quantos caracteres exitem
    print(f'Recebi os valores {num} que são ao todo {tam} números')# num para os numeros e tam para a quantidade de numeros guardados


cont(2, 3 , 5)
cont(5, 1)
cont(2, 5, 7, 9)

def so(*valores):
    s = 0
    for num in valores: # Para cada numero em valores
        s += num
    print(f'Somando os valores {valores} temos {s}')


so(2, 3 , 5)
so(5, 1)
so(2, 5, 7, 9)



#-----------------------------------------
def dobra(lst):
    pos = 0 # Variavel POS na posiçao 0
    while pos < len(lst): # Enquanto a posição for menor que o tamanho da lista
        lst[pos] *= 2 # lista na posição atual será o dobro dela
        pos += 1 # apos executgar essa tarefa vc dobra o valor do vetor


valores = [7,2,5,0,4]
dobra(valores)
print(valores)