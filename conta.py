class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += float(valor)

    def saca(self, valor):
        self.__saldo -= float(valor)

    def tranfere(self, valor, destino):
        self.saca(float(valor))
        destino.deposita(float(valor))

