# DICIONARIOS

Dicionario = {} #forma de criar um dicionário

Dicionario2 = dict() #Forma de criar um Dicionário

# Diferença do dicionario é que você pode nomear os indices

dados = {'nome':'Pedro', 'idade':25} #nome vira o indice e pedro o Dado que vai para Nome
#idade vira indice e 25 vai para dentro do indice Idade

print(dados['nome'])   # Pedro com resultado
print(dados['idade']) # 25 como resultado

dados['sexo'] = 'M' # Irá criar um novo indice chamado sexo contendo o resultado M

del dados['idade'] #remove o indice idade

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'Gearge Lucas'
        }
print(filme.values())# Irá retornar todos os valores que são, StarWar, 1977, George Lucas
print(filme.keys())# Irá retornar somente as chaves que são, titulo, ano, diretor
print(filme.items())# Irá pegar todas as informaçoes, tanto os valores quanto as chaves

for k, v in filme.items():
    print(f'O {k} é {v}')# resposta da primeira rotação do for é O Título é Star Wars

# UTilizando uma lista  contendo um Dicionario dentro

locadora = []
locadora.append(filme)
print(locadora[0['ano']]) # saida 1977


#########################################

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #O Gustavo tem 22 anos

for k in pessoas.keys():
    print(k) # Resposta nome, sexo, idade
for k in pessoas.values():
    print(k) # Resposta Gustavo, M, 22
for k, v in pessoas.items():
    print(f'{k} = {v}') # Resposta nome = Gustavo, sexo = M, idade = 22

del pessoas['sexo'] #Apaga indice sexo

pessoas['nome'] = 'Leandro' # irá trocar nome de Gustavo para Leandro

pessoas['peso'] = 98.5 # irá adicionar uma chave peso de valor 98.5


#CRIAR UM DICIONARIO DENTRO DE UMA LISTA
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]) # uf': 'Rio de Janeiro', 'sigla': 'RJ'
print(brasil[1]) # 'uf': 'São Paulo', 'sigla': 'SP'

print(brasil[0]['uf']) # Rio de Janeiro

####################
estado = dict()
brasil1 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil1)
for e in brasil1:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()