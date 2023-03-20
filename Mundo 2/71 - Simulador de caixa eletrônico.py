#Simulador de caixa eletrônico, utilizando apenas notas de 50, 20,10 e 1
from math import floor
print('Simulador de Caixa Eletrônico')

valor = int(input('Qual valor do saque? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if totced == 0:
            break
