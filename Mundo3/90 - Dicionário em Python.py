# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

#dicionario = {}
#dicionario['nome'] = str(input(('Nome: ')))
#dicionario['media'] = float(input('Média: '))
#print('-=' * 30)
#for k, v in dicionario.items():
   # print(f'{k} é igual a: {v}')
   # if dicionario['media'] >= 6:
    #    dicionario['situação'] = 'aprovado'
    #else:
    #    dicionario['situação'] = 'reprovado'
#print(f'situação é igual {dicionario["siuação"]}')

###################################################

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a: {v}')