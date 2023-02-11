#### Estrutura de repetição While

while not APPLE:
    pass
pega

----------------------------------------------

while not APPLE:
    if caminho:
        passo
    if espaço:
        pula
    if COIN:
        pega
Pega

-----------------------------------------------

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')


-----------------------------------------------------
n = 1
while n ! = 0:
    n = int(input('Digite um valor: '))
    print(n)
print('Fim')

------------------------------------------------------
r = 'S'
while r =='S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')

-------------------------------------------------------

n = 1
par = impar = 0
while n != 0
    n = int(input('Digite um valor: '))
    if n != 0: #' Para não contar o zero como par '
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} números pares e {} números ímpares!' .format(par, impar))