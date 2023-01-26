distancia = int(input('Qual sera a distancia percorrida? '))
if distancia <= 200:
    print('É cobrado 0,50 centavos por KM Rodado em viagens até 200Km')
    valor1 =distancia * 0.50
    print('O valor da viagem é: {:.2f} Reais' .format(valor1))
else:
    print('É cobrado 0,45 centavos por KM rodado em viagens acima de 200Km')
    valor2 = distancia * 0.45
    print('O valor da viagem é : {:.2f} Reais' .format(valor2))