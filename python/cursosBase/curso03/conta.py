class Conta():
    def __init__(self, titular, saldo, conta, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__conta = conta
        self.__limite = limite

    def pegar_estrato(self):
        print("Olá {} o seu saldo é de: {} RS".format(self.__titular, self.__saldo))

    def __pode_sacar(self):
        return valor <= (self.__limite + self.saldo)

    def sacar(self, valor):
        if(conta.__pode_sacar()):
            self.__saldo -= valor
        else:
            print("Olá {} o valor de {} RS a ser sacado excede o limíte de {} RS".format(self.__titular, valor, self.__limite))

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def conta(self):
        return self.__conta

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return 001
