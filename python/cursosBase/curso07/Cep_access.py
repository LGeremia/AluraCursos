import requests

class AddressSearch:
    def __init__(self, cep):
        cep = str(cep)
        if self.verify_cpf(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def verify_cpf(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def get_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        data = r.json()
        return (
            data["bairro"],
            data["localidade"],
            data["uf"]
        )