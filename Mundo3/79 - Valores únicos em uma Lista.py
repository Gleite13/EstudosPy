# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    n = (int(input('Digite um numero: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Esse valor ja esta na lista')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N)')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os valores adicionados foram {sorted(lista)}')