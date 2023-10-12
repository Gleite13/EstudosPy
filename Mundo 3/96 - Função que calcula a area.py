def area(a, b):
    ar = a * b
    print(f'A área de um de terreno {a} x {b} é de {ar}m²')


print('Controle de Terrenos')
print('-' * 10)
a = float(input('LARGURA (M): '))
b = float(input(('COMPRIMENTO (M): ')))
area(a, b)
