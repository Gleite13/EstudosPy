# Faça um programa que tenha uuma função chamada funçao maior(), que receba
# varios parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from random import randint
from time import sleep

def maior(* num):
    cont = maior = 0
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor

    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')

maior(2,1,5,6)

#VER AULA DO EXERCICIO