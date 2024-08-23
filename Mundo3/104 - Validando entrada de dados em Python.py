#Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input()
# do Python, só que fazendo a validação para aceitar
# apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(num):
    str(input(num))
    if num.isnumeric():
        num = int(num)
    else:
        num = print('ERRO! Digite um número inteiro valido')
    return num



# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você Acabou de digitar o número: {n}')
print(n)

##########################################
def leiaInt2(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            ok = True
            valor = int(num)
        else:
            print('\033[0;31mErro! DIgite um número inteiro\033[m')
        if ok:
            break
    return valor

n2 = leiaInt2('Digite um número; ')
print(f'Você acabou de digitar {n2}')