numero = int(input('Digite o número que deseja converter: '))
print('Escolha a base de conversão:\n '
      '[1] Converter em Binario\n '
      '[2] Converter em Octal\n '
      '[3] Converter em Hexadecimal')
opcao = int(input('Sua Opção: '))
if opcao == 1:
      print('{} Convertido para binário é igual a {}' .format(numero, bin(numero)[2:]))
elif opcao == 2:
      print('{} Convertido para octal é igual a {}' .format(numero, oct(numero)[2:]))
elif opcao == 3:
      print('{} Convertido para hexadecimal é igual a {}' .format(numero, hex(numero)[2:]))
else:
      print('Opção invalida')