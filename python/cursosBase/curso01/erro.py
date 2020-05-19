from models import *
try:
    arquivo = open('perfis.csv', 'r')
    valores = arquivo.readline().split(',')
    print('abriu')
    arquivo.close()
except (IOError, TypeError) as error:
    print(error)