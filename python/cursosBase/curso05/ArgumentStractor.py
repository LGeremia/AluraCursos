class ArgumentStractor:
    def __init__(self, url):
        if self.validated_url(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")
    
    @staticmethod
    def validated_url(url):
        if url and url.startswith("https://www.bytebank.com.br"):
            return True
        else:
            return False

    #caso print o len(objeto) irá retornar o tamanho da url 
    def __len__(self):
        return len(self.url)

    #caso print o objeto irá retornar um texto informando sobre os dados contidos na url
    def __str__(self):
        origin_currency, destiny_currency = self.stract_argument()
        represetation = "Valor: {} \nMoeda origem: {} \nMoeda destino: {}".format(self.find_value(), origin_currency, destiny_currency)
        return represetation

    #caso faça objeto == outro_objeto irá comparar se as urls são iguais
    def __eq__(self, comparation):
        return self.url == comparation.url

    #esse método recebe a url e a fatia entre dois tipos de moeda, a originária(origin_currency)
    #e a de destino(destiny_currency), para isso é definido os valores de cada indice iniciais e finais
    def stract_argument(self):
        origin = "moedaorigen="
        destiny = "moedadestino="
        initial_index_origin = self.find_initial_index(origin)
        final_index_origin = self.url.find("&")
        #aqui foi feito diferente pois tem que pular os primeiros valores de busca "=" e "&" da url
        #fazendo com que a busca inicie de onde encontrou nas variáveis anteriores
        initial_index_destiny = self.find_initial_index(destiny)
        final_index_destiny = self.url.find("&valor")

        origin_currency = self.url[initial_index_origin:final_index_origin]
        destiny_currency = self.url[initial_index_destiny:final_index_destiny]

        return origin_currency.title(), destiny_currency.title()

    def find_initial_index(self, sub_str):
        return self.url.find(sub_str) + len(sub_str)

    def find_value(self):
        value_finder = "valor="
        value = self.url[self.find_initial_index(value_finder):]
        return value
