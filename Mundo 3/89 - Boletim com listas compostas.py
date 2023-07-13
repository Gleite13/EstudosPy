# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

# bagaça ainda nao saiu mas vai!!!!


alunos = []
temp = []
temp2 = []
todos = 999
while True:
    for l in range(0, todos):
        temp[l].append(str(input('Nome: ')))
        for c in range(0, 2):
            temp[c] = int(input(f'Nota {c+1}: '))
        alunos.append(temp[:])
        temp.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break



print(alunos)
print(alunos[l])