r1 = float(input('Digite e primeira reta: '))
r2 = float(input('Digite a segunta reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima não podem formar um triângulo')