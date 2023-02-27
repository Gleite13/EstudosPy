# Progressão Aritmética utilizando while

s = 0
cont = 0
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
while cont != 10:
    cont += 1
    s = primeiro + (cont-1)*razao
    print(s, end=' ')