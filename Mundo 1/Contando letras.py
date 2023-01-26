frase = str(input('Digite uma frase: ')).upper() .strip()
print('Existem {} de A na frase' .format(frase.count('A')))
print('A primeira letra "A" aparece no caracter {}' .format(frase.find('A')+1))
print('A ultima letra "A" aparece no caracter {}' .format(frase.rfind('A')+1))