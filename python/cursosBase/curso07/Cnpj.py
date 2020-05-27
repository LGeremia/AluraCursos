from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, document):
        if self.validated_cnpj(document):
            self._cnpj = str(document)
        else:
            raise ValueError("CNPJ inválido!")
        self._formated_cnpj = self.format_cnpj()
    
    def validated_cnpj(self, document):
        if len(str(document)) >= 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(document)
        else:
            raise ValueError("Quantidade de digitos errada!!")

    def format_cnpj(self):
        mask = CNPJ()
        return mask.mask(self._cnpj)

    def __str__(self):
        return 'O CNPJ é: {}'.format(self._formated_cnpj)