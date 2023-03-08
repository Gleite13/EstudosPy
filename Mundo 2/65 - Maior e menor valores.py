# Contar maior, menor valor e média

cond = 'S'
nota = soma = cont = menor = maior = 0
while cond == 'S':
    nota = int(input('Digite sua nota: '))
    cond = str(input('Deseja continuar? [S/N]: ').upper())
    soma += nota
    cont += 1
    media = soma/cont
    if nota > maior:
        maior = nota
    else:
        menor = nota
print('a media {:.2f} e a contagem  de notas sâo  {} ' .format(media, cont))
print('A maior nota é {} e a menor {}' .format(maior, menor))
