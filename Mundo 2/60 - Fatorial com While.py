# Formas de usar o calculo de fatorial IMPORT MATH, WHILE e FOR

from math import factorial
n = int(input('Fatorial de: '))
f = factorial(n)
print('O fatorial de {} é {}' .format(n, f))


######################################################


n1 = int(input('Fatorial de: '))
count = n1
fact = 1
print('Calculando {}! = ' .format(n1))
while count > 0:
    print('{} ' .format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fact *= count
    count -= 1
print('{}' .format(fact))

#################################################

n2 = int(input('Fatorial de: '))
cont = n2
fato = 1
for c in range(cont, 0, -1):
    print('{} ' .format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    fato *= cont
    cont -= 1
print('{} ' .format(fato))