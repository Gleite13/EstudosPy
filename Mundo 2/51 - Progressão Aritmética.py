s = 0
print('='*30)
print('         Calculo de PA           ')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razao = int(input(('Razão: ')))
for c in range(1, 11):
    s = primeiro + (c-1)*razao
    print(s, end=' ')
print('Fim')