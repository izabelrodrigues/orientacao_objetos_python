class Conta:

    # Building the Class Constructor
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def obter_extrato(self):
        print("A conta {} do titular {} possui o saldo de R${}".format(self.__numero, self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __verifica_limite_disponivel(self, valor_saque):
        return valor_saque <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        if self.__verifica_limite_disponivel(valor):
            self.__saldo -= valor
            print("Retirada efetuada com sucesso!")
            self.obter_extrato()
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def obter_codigo_bancos():
        return {'BB': '001', 'CAIXA': '104', 'ITAU': '341'}
