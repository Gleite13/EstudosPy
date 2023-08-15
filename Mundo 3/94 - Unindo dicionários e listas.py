# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B)
# A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

dicionario = {}
lista = []
soma = media = 0
while True:
    dicionario['nome'] = str(input('Nome: '))
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dicionario['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F')
    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    dicionario.clear()
    resp = str(input('Deseja Continuar? [S/N]: '))
    if resp in 'Nn':
        break
    elif resp not in 'Ss':
        print('ERRO! Por favor, digite M ou F.')
media = soma / len(lista)

print(f'A) Ao todo temos {len(lista)} cadastradas')
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista: # para lista na posição p
    if p['sexo'] in 'Ff': # se na posição p['sexo'] for Ff
        print(f'{p["nome"]} ', end='')# mostre p na posição nome
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in lista: #para lista na posição p
    if p['idade'] >= media: # Se na posição p['idade'] for maior ou igual a media
        print('        ')
        for k, v in p.items(): # no posição k, e o valor v na posição dos itens
            print(f'{k} = {v}; ', end='')# ira mostrar somente quem estiver acima da media e a posição
        print()



print(dicionario)
print(lista)


