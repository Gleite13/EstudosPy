from datetime import date
data = int(input('Que ano quer analisar? Digite 0 para verificar o ano atual: ' ))
if data == 0:
    data = date.today().year
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print('O ano {} é Bissexto'.format(data))
else:
    print('O ano {} não é Bissexto' .format(data))