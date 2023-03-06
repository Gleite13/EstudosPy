# Tratando vários valores

print('Tratando Varios Valores')
cond = valor = cont = 0
print('Digite 999 para finalizar a soma')
cond = int(input('Digite o valor para somar: '))
while cond != 999:
    valor += cond
    cont += 1
    cond = int(input('Digite o valor para somar: '))
print('Foram contados {} valores e o total é: {}' .format(cont, valor))

