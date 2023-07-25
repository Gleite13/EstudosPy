#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho (0) não tem: '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: '))
else:
    cadastro['ctps'] = 'Não Possui'
for k, v in cadastro.items():
    print(f'  - {k} tem valor {v} ')
print(cadastro)

#FINALIZAR AINDA