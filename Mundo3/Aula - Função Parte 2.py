help() #Função que mostra o que cada comando faz

print(input.__doc__) #mostra a coumentação do comando imput

# DOCSTRINGs


def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio do contador
    :param f: Fim do contador
    :param p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim!')


help(contador) # ira exibir a doctring feita pela função
contador(2,10,2)

# Parametrod Opcionais

def somar(a=0,b=0,c=0): #dar valor 0 aos paramentros
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A Soma vale {s}')

somar(3,2,5)
somar(8,4) #utiliza apenas os parametros a e b, automaticamente C recebe 0
somar(b=4,c=2) # pode utilizar o parametro desejado


# ESCOPO DE VARIAVEIS
def teste():
    x = 8 # X é uma escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2
print(f'No programa principal, m vale {n}')
teste() # N é escopo global



def test(b):
    b += 4      # B estará valendo 9 pois recebe como parametro de A valendo 5 sendo feito a soma
    c = 2       # C estará valendo 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')



a = 5     # ESCOPO GLOBAL
teste(a)
print(f'A fora vale {a}')  # A vale 5



######

def test2(b):
    a = 8       # Irá ser criado uma variavel local A valendo 8
    b += 4      # B estará valendo 9 pois recebe como parametro de A valendo 5 sendo feito a soma
    c = 2       # C estará valendo 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')



a = 5     # ESCOPO GLOBAL
test2(a)
print(f'A fora vale {a}')  # A vale 5

#############

def test3(b):
    global a # Neste caso ele fará com que a letra A se torne global valendo 8 e não 5
    a = 8
    b += 4      # B estará valendo 9 pois recebe como parametro de A valendo 5 sendo feito a soma
    c = 2       # C estará valendo 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')



a = 5     # ESCOPO GLOBAL
teste(a)
print(f'A fora vale {a}')  # A vale 8 por conta do global A dentro da função


# Retorno de valores
def somar2(a=0,b=0,c=0):
    s = a + b + c
    return s

resp = somar2(3,2,5)
# Ou
print(somar2(3,2,5))
# Ou
r1 = somar2(3,2,5)
r2 = somar2(1,7)
r3 = somar2(4)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1)
        f *= c
    return f


n = int(input('Digite um número :'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
# OU
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados dos fatoriais são {f1}, {f2} e {f3}')



def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero'))
print(par(num))
# OU
if par(num):
    print('É Par!')
else:
    print('Não é par')