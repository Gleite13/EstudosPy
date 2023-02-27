# Progressão Aritmética utilizando while melhorado

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro temo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ' .format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos' .format(total))