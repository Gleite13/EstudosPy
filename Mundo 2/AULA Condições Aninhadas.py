nome = str(input('Diga o seu nome: '))
if nome == 'Erika':
    print('Que nome bonito!!')
elif nome == 'Emily' or 'Guilherme':
    print('Vocês são da familia Leite')
else:
    print('Que nome normal')
print('Tenha um bom dia {}' .format(nome))