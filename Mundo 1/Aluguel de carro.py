dias = float(input('Por quantos dias foi alugado o carro? '))
km = float(input('Quantos Km foram rodados? '))
a = dias * 60
b = km * 0.15
total = a + b
print('O valor total a pagar é {}R$ '.format(total))