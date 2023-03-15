# Coletar diversas informaçoes idade, sexo,
#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

cont = 0
idadecont = 0
femcont = 0
maior = 0
while True:
    sexo = str(input('Masculino ou Femino? [M/F]: ').strip().upper()[0])
    cont += 1
    if sexo == 'M':
        idadecont += 1
    elif sexo == 'F' and idade < 20:
        femcont += 1
    elif sexo != 'M' and sexo != 'F':
        break
    idade = int(input('Quantos anos você tem? '))
    if idade > 18:
        maior += 1
print(f'''Foram cadastrados {maior} maiores de idade
Foram Cadastrados {idadecont} homens
Foram cadastradas {femcont} menor(s) de 20 anos''')

##########################################################


tot18 = totH = totM20 = 0
while True:
    idade1 = int(input(('Idade: ')))
    sexi = ' '
    while sexi not in 'MF':
        sexi = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade1 >= 18:
        tot18 += 1
    if sexi == 'M':
        totH += 1
    if sexi == 'F' and idade1 < 20:
        totM20

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao total temos {totH} homens cadastrados')
print(f'E Temos {totM20} mulheres menores de 20 anos')