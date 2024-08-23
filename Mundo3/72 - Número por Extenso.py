# Número por extenso utilizando Tuplas

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
while n not in range (0, 21):
    n = int(input('Tenten novamente, Digite um número de 0 a 20: '))
print(f'O número pedido foi {numeros[n]}')

#---------------------------------------------------

while True:
    n = int(input('Digite um número de: 0 a 20: '))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Conitnuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'O número pedido é {numeros[n]}')