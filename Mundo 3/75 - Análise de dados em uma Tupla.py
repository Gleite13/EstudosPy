#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.


n1 = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1}º posição')
else:
    print('Não possui números 3 na tupla')
print('Os valores pares digitados: ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ', )