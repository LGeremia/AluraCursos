from excecoes import LanceInvalido

class Usuario:
    def __init__(self, nome, carteira):
        self.__carteira = carteira
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_nao_eh_valido(self, valor):
        return self.__carteira < valor

    def propoe_lance(self, leilao, valor):
        if self._valor_nao_eh_valido(valor):
            raise LanceInvalido("Usuário não tem saldo suficiente para dar um lance!")
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def _nao_tem_lances(self):
        return not self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar 2 lances seguidos!")

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O lance atual deve ter valor maior que o lance anterior")

    def _lance_eh_valido(self,lance):
        return self._nao_tem_lances() or self._usuarios_diferentes(lance) and self._valor_maior_que_lance_anterior(lance)

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if self._nao_tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance=lance.valor
            self.__lances.append(lance)
