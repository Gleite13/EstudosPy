n1 = float(input('Digite o valor da primeira reta: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceita reta: '))
if n1 < n2 + n3 and n2 < n1 +n3 and n3 < n1 + n2:
    if n1 != n2 != n3:
        print('Esses valores formam um triângulo Escalêno')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
        print('Esses valores formam um triândulo Isósceles')
    elif n1 == n2 == n3:
        print('Esses valores formam um triângulo Equilatero')
else:
    print('Esses valores não formam um reta.')
