from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano em que vc nasceu: '))
idade = atual - nasc
print('Quem nasceu {} tem {} anos no ano atual de {}' .format(nasc, idade, atual))
if idade == 18:
    print('Você esta na idade de alistamendo')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos para o alistamento' .format(saldo))
    ano = idade + saldo
    print('Seu alistamento sera em {}' .format(ano))
else:
    saldo = idade - 18
    print('Você é maior de 18 anos, ja devia ter se alistado há {} anos' .format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}' .format(ano))