from Cnpj import Cnpj
from Cpf import Cpf

class Document:

    @staticmethod
    def generate_document(document):
        if(len(document) == 11):
            return Cpf(document)
        elif(len(document) == 14):
            return Cnpj(document)
        else:
            raise ValueError("Documento inválido!!")
