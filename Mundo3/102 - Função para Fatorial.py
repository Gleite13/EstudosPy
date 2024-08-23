def fatorial(num=1, show=False):
    """
    Programa que Mostra o fatorial de um numero.
    :param num: O número a ser Calculado
    :param Show: (Opcional) Mostrar ou não a conta
    :return: o valor do Fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} x  ', end='')

    return f


n = int(input('Digite um número: '))
print(fatorial(n, show=False))


###################################

def fatorial1(num=1, show=False):
    """
    Programa que Mostra o fatorial de um numero.
    :param num: O número a ser Calculado
    :param Show: (Opcional) Mostrar ou não a conta
    :return: o valor do Fatorial
    """
    f = 1
    for c in range(num, 0, -1):

        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


print(fatorial1(5, show=True))