class ArgumentStractor:
    def __init__(self, url):
        if self.validated_url(url):
            self.url = url
        else:
            raise LookupError("Url inválida!")
    
    @staticmethod
    def validated_url(url):
        if url:
            return True
        else:
            return False

    #esse método recebe a url e a fatia entre dois tipos de moeda, a originária(origin_currency)
    #e a de destino(destiny_currency), para isso é definido os valores de cada indice iniciais e finais
    def stract_argument(self):
        initial_index_origin = self.find_initial_index("moedaOrigen=")
        final_index_origin = self.url.find("&")
        #aqui foi feito diferente pois tem que pular os primeiros valores de busca "=" e "&" da url
        #fazendo com que a busca inicie de onde encontrou nas variáveis anteriores
        initial_index_destiny = self.find_initial_index("moedaDestino=")
        final_index_destiny = self.url.find("&",(final_index_origin+1))

        origin_currency = self.url[initial_index_origin:final_index_origin]
        destiny_currency = self.url[initial_index_destiny:final_index_destiny]

        return origin_currency, destiny_currency

    def find_initial_index(self, currency):
        return self.url.find(currency) + len(currency)
