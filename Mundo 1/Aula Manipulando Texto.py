frase = 'Curso em Vídeo Python'

print(frase[9:13])  #Inicia a frase do caracter 9 e vai até o 13

print(frase[9:21])  #Inicia a frase do caracter 9 e vai até o 21

print(frase[9:21:2])  #Inicia a frase do caracter 9 até o 21 pulando de 2 em 2 caracteres

print(frase[:5])  #Inicia a frase do primeiro caracter até o caracter 5

print(frase[15:])  #Inicia a frase a partir do caracter 15 até o final

print(frase[9::3])  #Inicia a frase do caracter 9 pulando de 3 em 3

print(len(frase))  #Conta quantos caracteres possuem na frase

print(frase.count('o'))  #Conta quantos 'o' existem na frase com caracteres possui

print(frase.count('o',0,13))  #Irá contar o numero de 'o' entre os caracteres de 0 a 13

print(frase.find('deo'))  #Ira achar em que numero começa o primeiro caracter com deo

print(frase.find('Android'))  #Caso nao haja a palavra na frase ira apresentar o valor -1

print('curso' in frase)  #Diz se existe a palavra curso no texto com true ou false

#Transformações

print(frase.replace('Python','Android'))  #Substitui a palavra Python da frase por Android

print(frase.upper())  #deixa todos os caracteres da frase em maiúsculo

print(frase.lower())  #deixa todos os caracteres da frase minúsculo

print(frase.capitalize())  #deixa o primeiro caracter da frase em maiúsculo

print(frase.title())  #A cada quebra de palavra ele deixa o inicio da palavra maiusculo

frase1 = '  Aprenda Python   '

print(frase1.strip())  #Elimina os espaços no inicio e no final do texto

print(frase1.rstrip())  #Elimina os espaços do lado final a direita do texto

print(frase1.lstrip())  #Elimina os espaços do inicio a esquerda do texto

print(frase.split())  #Cria uma divisão dos caracteres usados na frase, colocando cada uma das palavras em uma lista

#JUNÇÃO

divido = frase.split()
print(divido[0])
print(divido[2][3])




