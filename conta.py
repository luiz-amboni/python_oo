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

    def __pode_sacar(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel_saque

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= float(valor)
            print("Você sacou R${}. O valor atual da sua conta é de R${}".format(valor, self.__saldo))
        else:
            print("O valor R${} passou o limite".format(valor))

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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @limite.setter
    def limite(self, limite):
        print("Limite atualizado de R${} para R${}".format(self.__limite, limite))
        self.__limite = limite


