def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": float(saldo), "limite": float(limite)}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("saldo {}".format(conta["saldo"]))
<<<<<<< HEAD

=======
>>>>>>> 999883c9ea4d4062e2510de078b584a0c926876b
