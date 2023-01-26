#Utilizando If e Else

tempo = int(input('Quantos anos seu carro tem? '))
if tempo <= 3:
    print('Seu Carro é novo')
else:
    print('Seu carro é velho')
print('---FIM---')

#-- Condição Simplificada

tempo1 = int(input('Quantos anos seu carro tem? '))
print('Seu carro é novo' if tempo1<=3 else 'Seu carro é velho')
print('---FIM---')

#----Praticando

n1 = float(input('Digite a primeira nota: '))
n2 = float(input(('Digite a segunda nota: ')))
m = (n1+n2)/2
print('A sua media é {:.1f} '.format(m))
if m >= 6.0:
    print('Você esta aprovado')
else:
    print('Você esta de recuperação')