from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
if idade <= 9:
    print('Você tem {} e é um atleta mirim' .format(idade))
elif idade > 9 or idade <= 14:
    print('Você tem {} e é um atleta infantil' .format(idade))
elif idade > 14 or idade <= 19:
    print('Você tem {} e é um atleta Junior' .format(idade))
elif idade == 20:
    print('Você tem {} e é um atleta Senior' .format(idade))