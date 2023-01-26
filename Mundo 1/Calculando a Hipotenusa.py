from math import hypot
cadj = float(input('Digite o valor do cateto adjacente: '))
copo = float(input('Digite o valor do cateto oposto: '))
hipo = hypot(cadj, copo)
print('A hipotenusa é {:.2f} ' .format(hipo))
