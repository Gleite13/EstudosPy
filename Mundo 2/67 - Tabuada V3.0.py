#Verificar tabuada de algum número, interferindo caso o numero for negativo

while True:
    n = int(input('Qual Tabuada você deseja saber? '))
    if n == -n:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')