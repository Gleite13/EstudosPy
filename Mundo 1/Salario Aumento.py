salario = float(input('Diga o valor do seu salário: '))
if salario >= 1250.00:
    novo = salario * 1.1
    print('O valor do salário reajustado em 10% é {} ' .format(novo))
else:
    novo = salario * 1.15
    print('O valor do salário reajustado em 15% é {} ' .format(novo))