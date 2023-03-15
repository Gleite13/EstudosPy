# Ler o valor o nome e o preço de varios produtos programa deve perguntar se deseja continuar ou não
#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

total = tot10 = cont = menor =  0
barato = ' '
while True:
    nome = str(input('Qual o nome do produto: '))
    valor = float(input('Qual o valor do produto '))
    total += valor
    cont += 1
    if valor > 1000:
        tot10 += 1
    if cont == 1 or valor < menor: # faz com que o menor produto seja adiocionado as variasveis
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total das compras é de {total:.2f}R$')
print(f'Foram visualizada(s) {tot10} compras acima de mil reais')
print(f'O Produto mais barato foi {barato} que custa R${menor:.2f}')