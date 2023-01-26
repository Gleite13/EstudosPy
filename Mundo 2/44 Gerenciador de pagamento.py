print('====LOJAS LEITE====')
compra = float(input('Qual o valor total da compra? '))
print('Formas de pagamento:\n'
      '1 para Dinheiro ou Cheque\n'
      '2 para Cartão \n')
pag = int(input('Digite a forma de pagamento: '))
if pag == 1 or pag == 2:
      if pag == 1:
            print('Pagamentos em Dinheiro ou Cheque tem 10% de desconto')
            desc = compra * 0.9
            print('O Valor com desconto é de: {}R$' .format(desc))
      elif pag == 2:
            print('1 para debito\n'
                  '2 para crédito\n')
            cartao = int(input('Digite a opção desejada: '))
            if cartao == 1:
                  print('No Débito você possui 5% de desconto')
                  desc = compra * 0.95
                  print('O Valor com o desconto é de: {}R$' .format(desc))
            elif cartao == 2:
                  print('Deseja parcelar?\n'
                        '1 para SIM\n'
                        '2 para Não\n')
                  cred = int(input('Digite a opção desejada: '))
                  if cred == 1:
                        print('Parcelas a partir de 3x tem reajuste de 20%')
                        parc = int(input('Deseja parcelar em quantas vezes? '))
                        if parc <= 2:
                              print('O valor total é de {}R$' .format(compra))
                        else:
                              cred = compra * 1.2
                              print('O valor com 20% de juros é de {}R$' .format(cred))
                  elif cred == 2:
                        print('O valor todal da compra é de {}'.format(compra))

                  else:
                        print('Opção Invalida')
            else:
                  print('Opção Ivalida')
      else:
            print('Opção Ivalida')
else:
      print('Opção Ivalida')