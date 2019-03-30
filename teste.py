def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titula": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] +=valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("A conta {} possui o saldo de R${}".format(conta["numero"], conta["saldo"]))

