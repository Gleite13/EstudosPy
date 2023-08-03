# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B)
# A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

dicionario = {}
lista = []
while True:
    dicionario['nome'] = str(input('Nome: '))
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: '))
        if dicionario['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F')
    dicionario['idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())
    dicionario.clear
    resp = str(input('Deseja Continuar? [S/N]: '))
    if resp in 'Nn':
        break
    elif resp not in 'Ss':
        print('ERRO! Por favor, digite M ou F.')
print(dicionario)
print(lista)
teste