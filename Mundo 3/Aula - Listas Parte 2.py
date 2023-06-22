# Listas AULA parte 2

dados = ['Pedro', 25]
pessoas = list()

pessoas.append(dados[:]) # Faz um copia da lista de dados em pessoas valendo Pedro e
                        # 25 como o valor 0 podendo seguir dai em diante

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] #a cada [] dentro da propria
                                                # lista contem o valor 0, 1, 2
print(pessoas[0][0]) #  Irá mostrar dentro da primeira lista, a primeira opção dentro da lista
                    # o nome Pedro irá aparecer na Tela

print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]

for p in pessoas:
    print(p) #irá mostrar todas as pessoas em p
for p in pessoas:
    print(p[0]) # irá mostrar somente nomes cadastrados na posição 0
for p in pessoas:
    print(p[1]) # irá mostrar somente a idade cadastrados na posição 1
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade') # mostrar dados na posição 0 e 1 formatados

galera = list() # Lista onde será guardados os Dados
dado = list() # lista de apoio
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # irá guardar o nome e a idade da lista dado fazendo um copia pelo uso do [:]
    dado.clear() # Limpa toda a lista dado

for p in galera: #para na posição de quem é maior de 21 anos
    if p[1] >= 21: # se P na posição 1 é maior ou igual a 21
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1