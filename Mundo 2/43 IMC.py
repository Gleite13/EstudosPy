peso = float(input('Diga o seu peso: '))
altura = float(input('Diga a sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC é {:.2f}, você esta abaixo do peso' .format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}, você esta no peso ideal' .format(imc))
elif 25 >= imc < 30:
    print('Seu IMC é {:.2f}, você esta em sobrepeso ' .format(imc))
elif 30 >= imc < 40:
    print('Seu IMC é {:.2f}, você esta com obesidade' .format(imc))
else:
    print('Seu IMC é {:.2f}, você esta com obesidade mórbida' .format(imc))