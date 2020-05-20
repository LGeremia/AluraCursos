from ArgumentStractor import *

url = "https://www.bytebank.com.br/cambio?moedaOrigen=real&moedaDestino=dolar&valor=1500"
print(ArgumentStractor.validated_url(url))

teste = ArgumentStractor(url)
teste.stract_argument()

origin_currency, destiny_currency = teste.stract_argument()
print(origin_currency, destiny_currency)