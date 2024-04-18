#Crie um programa que tenha uma função chamada voto() que vai receber como
#parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
#indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições


def voto():
    from datetime import date
    atual = date.today().year
    nasc = int(input('Digite o ano que você nasceu: '))
    idade = atual - nasc


    if idade >= 65:
        print('Voto Opcional')
    elif idade >= 18 and idade < 65:
        print('Voto Obrigatorio')
    else:
        print('Voto Negado')

    return idade

voto()


#################

def voto2(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatorio'


nasc = int(input('Em que ano você nasceu? '))
print(voto2(nasc))
print(voto2(2000))