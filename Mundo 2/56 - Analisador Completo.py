# 56 - Desenvolva um programa que leia o nome, idade e exo de 4 pessoas
# Mostre a media de idade do grupo, qual o nome do homem mais velho e quantas mulheres com menos de 20 anos

velho = ''
soma = 0
maior = 0
cont = 0
for c in range(1, 5):
    print('-=-'*3)
    nome = str(input('Nome da {}º pessoa: ' .format(c)))
    sexo = str(input('Masculino ou Feminino [M/F]: ' .format(c) .upper()))
    idade = int(input('Idade da {}º pessoa: ' .format(c)))

    media = soma / c
    if sexo == 'M' and idade > maior:
        maior = idade
        velho = nome
    soma += idade
    if sexo == 'F' and idade < 20:
        cont += 1

print('A média de idade do grupo é: {} ' .format(media))
print('O nome do homem mais velho é {}' .format(velho))

if cont == 0:
    print('Não há mulheres no no grupo')
else:
    print('Há {} mulher(s) menores de 20 anos' .format(cont))