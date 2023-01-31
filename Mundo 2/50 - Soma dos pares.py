s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um numero: '))
    cont += 1
    if num % 2 == 0:
        s += num
print('A foram feito {} contagens e a soma dos pares é: {}' .format(cont, s))


