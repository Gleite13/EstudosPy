# Ler o valor o nome e o preço de varios produtos programa deve perguntar se deseja continuar ou não
#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

total = tot10 = 0
barato = ' '
while True:
    nome = str(input('Qual o nome do produto: '))
    valor = float(input('Qual o valor do produto '))
    total += valor
    if valor > 1000:
        tot10 += 1
    if valor < 


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total das compras é de {total:.2f}R$')
print(f'Foram visualizada(s) {tot10} compras acima de mil reais')