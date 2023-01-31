cont = 0
num = int(input('Digite um numero: '))
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[34m', end='')
    else:
        print('\033[35m', end='')
    print('{} '.format(c), end='')
if cont == 2:
    print('\033[mEste é um numero primo\033[m')
else:
    print('\n\033[mEste numero foi dividido {} vezes\033[m' .format(cont))