import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro')
else:
    print('Tudo Ok')



###########################

from urllib.request import urlopen

with urlopen("https://www.pudim.com.br") as response:
    body = response.read()

print(body[:15])