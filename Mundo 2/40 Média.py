print('----Média escolar----')
n1 = float(input('Digite o valor da primeira prova: '))
n2 = float(input('Digite o valor da segunda prova: '))
media = (n1+n2)/2
if media >= 7:
    print('A sua média é {:.2f}, você esta aprovado!' .format(media))
elif media >=5 or media <=6.9:
    print('A sua média é {:.2f}, você esta de recuperação.' .format(media))
else:
    print('A sua média é {:.2f}, você esta reprovado' .format(media))