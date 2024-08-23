def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n033[31mUsuario preferiu não digitar esse numero\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n033[31mUsuario preferiu não digitar esse numero\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e real {n2}')