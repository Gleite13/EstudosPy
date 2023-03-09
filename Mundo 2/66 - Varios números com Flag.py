# Tratando varios valores utilizando break

print('Tratando varios valores: ')
print('Digite 999 para finalizar o programa')
valor = cont = soma = 0
while True:
    valor = int(input('Digite o valor: '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'o Valor da soma dos números é de {soma}, foram contados {cont} números')
