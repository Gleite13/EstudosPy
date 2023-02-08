from datetime import date
atual = date.today().year
contador = 0
contador1 = 0
for c in range(1, 8):
    data = int(input('Digite o ano de nascimento da {}° pessoa: ' .format(c)))
    idade = atual - data
    if idade >= 21:
        contador += 1
    else:
        contador1 += 1
print('''Existem {} maiores de idade
Existem {} menores de idade''' .format(contador, contador1))