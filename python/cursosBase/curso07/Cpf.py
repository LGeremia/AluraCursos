from validate_docbr import CPF

class Cpf:
    def __init__(self, document):
        if self.validated_cpf(document):
            self._cpf = str(document)
        else:
            raise ValueError("CPF inválido!")
        self._formated_cpf = self.format_cpf()

    def validated_cpf(self, document):
        if len(str(document)) >= 11:
            validate_cpf = CPF()
            return validate_cpf.validate(document)
        else:
            raise ValueError("Quantidade de digitos errada!!")

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self._cpf)

    def __str__(self):
        return 'O CPF é: {}'.format(self._formated_cpf)