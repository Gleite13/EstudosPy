#ESTRUTURA DE REPETIÇÃO

for c in range(1,10):
    passo
pega

#######################

for c in range(0,3):
    passo
    pula
passo
pega

#######################

for c in range(0,3):
    if coin:
        pega
    else:
    passo
    pula
passo
pega

######################

for c in range(0,6):
    print(c)
print('fim')

########################

for c in range(0,7,2):  # Pula de dois em dois por conta do 2
    print(c)
print('Fim')

######################

for c in range(6,0,-1):  #Mostra o numero decrescente do 6 ao 1 por conta do -1
    print(c)
print('fim')

#######################

n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('Fim')

######################

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

#########################

for c in range(0, 3):
    n = int(input('Digite um valor: ')) # Vai pedir 3 vezes para repetir o valor
print('Fim')

#########################

s = 0
for c in range(0, 4):
    n = int(input('Digite um número')) ### Faz a soma dos numeros 4 vezes
    s += n  # s = s + n
print('O somatorio de todos os valores fois {}' .format(s))