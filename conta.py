class Conta:

    # Building the Class Constructor
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("A conta {} do titular {} possui o saldo de R${}".format(self.numero, self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
