casa = float(input('Qual o valor da casa?  '))
salario = float(input('Qual o salário do comprador? '))
ano = int(input('Por quantos anos deseja pagar?  '))
meses = ano*12
prestacao = casa / meses
if prestacao >  salario - (salario * 0.7):
    print('O valor das parcelas é maior 30% do salário')
else:
    print('O valor da pretação será de {:.2f} ao mes' .format(prestacao))
