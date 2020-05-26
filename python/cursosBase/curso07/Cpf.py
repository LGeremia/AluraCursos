class Cpf:
    def __init__(self, document):
        if self.validated_cpf(document):
            self.cpf = str(document)
        else:
            raise ValueError("CPF inválido!")
        self.format_cpf()

    def validated_cpf(self, document):
        if len(str(document)) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        first_part = self.cpf[:3]
        second_part = self.cpf[3:6]
        third_part = self.cpf[6:9]
        fourth_part = self.cpf[9:]
        self.formated_cpf = "{}.{}.{}-{}".format(first_part, second_part, third_part, fourth_part)