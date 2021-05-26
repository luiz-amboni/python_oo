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
        print("Limite atualizado de R${} para R${}".format(self.__limite, limite))
        self.__limite = limite
