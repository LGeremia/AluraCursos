import re

email1 = "teste teste teste 99999999"
email2 = "9999-9992 teste teste teste"
email3 = "teste 9999-9993 teste 00100-0000 teste"

'''
entre [] está os caracteres a serem procurados
entre as {} está a quantia de vezes que procura encontrar os caracteres procurados
o * diz se pode ou não existir o caracter a ser procurado
re.search procura a primeira ocorrência do padrão e precisa colocar o .group() para printar
re.findall procura todas as ocorrências do padrão e não precisa colocar o .group()
'''

template = "[0-9]{4,5}[-]*[0-9]{4}"
re_search = re.search(template, email1)
print(re_search.group())
re_search = re.findall(template, email2)
print(re_search)
re_search = re.findall(template, email3)
print(re_search)