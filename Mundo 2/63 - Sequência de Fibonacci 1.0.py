#Sequência de Fibonacci WHILE

print('Sequencia de Fibonacci: ')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
pausa = 1
print('{} -> {} ' .format(t1, t2), end=' ')
cont = 3 # 3 pois  t1, t2 e t3 ja valem na contagem
#     while pausa != 0:
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1  # faz com que o contador pare no valor de n
print(' -> Fim')
#    print('')
#    seq = t3
 #   pausa = int(input('Digite [1] para continuar os termos e [0] para sair: '))
 #   n = int(input('Quantos termos deseja adicionar: '))