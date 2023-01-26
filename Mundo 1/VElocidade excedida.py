velo = int(input('Qual foi a velocidade passada no radar? '))
if velo > 80:
    print('Você foi multado')
    multa = (velo - 80)*7
    print('O valor da multa é de {}RS'.format(multa))
print('Boa Viagem')