# Criando Menu de opções com exercicio utilizando While

print('''Digite dois números''')
x = 0
while x != 5:
    n1 = float(input('Diga o primeiro número: '))
    n2 = float(input('Diga o segundo número: '))
    print('Menu de Opções: ')
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números 
[5] Sair do Programa''')
    x = int(input('Digite uma opção: '))
    if x == 1:
        print('A soma dos valores é: {:.2f}' .format(n1+n2))
    if x == 2:
        print('A multiplicação dos valores é: {:.2f}' .format(n1*n2))
    if x == 3:
        if n1 > n2:
            print('O maior número é {}' .format(n1))
        if n2 > n1:
            print('O maior número é: {}' .format(n2))
        else:
            print('Números iguais.')
    if x == 4:
        print('Retornando ao menu...')
    if x == 5:
        print('Saindo do programa...')


