# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

# bagaça ainda nao saiu mas vai!!!!


alunos = []
temp = []
temp2 = []
todos = 999
while True:
    nome = str(input('Nome: '))
    temp.append(nome)
    for c in range (1, 3):
        nota = int(input(f'Nota {c}: '))
        temp2.append(nota)
    alunos.append(temp[:])
    alunos.append(temp2[:])
    temp.clear()
    temp2.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
for l in range(0, len(alunos)):
    for c in range(0, len(alunos)):
        print(alunos[l])
print(alunos)