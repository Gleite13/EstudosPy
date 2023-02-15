print('''Digite dois números''')
n1 = float(input('Diga o primeiro número: '))
n2 = float(input('Diga o segundo número: '))
print('Menu de Opções: ')
print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números 
[5] Sair do Programa''')

x = 0
while x != 5:
    x = int(input('Digite uma opção: '))
    if x == 1:
        print('A soma dos valores é: {:.2f}' .format(n1+n2))
    if x == 2:
        print('A multiplicação dos valores é: {:.2f}' .format(n1*n2))
    if x == 3:
        if n1 > n2:
            print('O maior número é {}' .format(n1))
        else:
            print('O maior número é: {}' .format(n2))


