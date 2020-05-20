from ArgumentStractor import *

url = "https://www.bytebank.com.br/cambio?moedaOrigen=real&moedaDestino=dolar&valor=1500"

teste = ArgumentStractor(url)
teste.stract_argument()

origin_currency, destiny_currency = teste.stract_argument()
value = teste.find_value()
print(origin_currency, destiny_currency)
print(value)
print(teste)