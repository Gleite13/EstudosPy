n = s = 0
while True:  #True faz com que faça um loop infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}' .format(s))
print(f'A soma vale {s}') #F strings sao usadas com o f antes do comentario e dentro dos colchetes usa a variavel

#############################

nome = 'José'
idade = 33
print(f'O {nome} tem {idade}. ')