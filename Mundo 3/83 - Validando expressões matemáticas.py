# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.

expr = str(input('Digite a expressã: '))
lista = []
for simb in expr:
    if simb =='(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0 # se a lista for maoir que 0
            lista.pop() # apagar o ultimo numero