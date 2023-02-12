sexo = str(input('Digite o seu sexo: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso' .format(sexo))