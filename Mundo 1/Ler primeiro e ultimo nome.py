f = str(input('Digite seu nome: ')).strip()
frase = f.split()
print('Primeiro: {}' .format(frase[0]))
print('Ultimo: {}' .format(frase[len(frase)-1]))