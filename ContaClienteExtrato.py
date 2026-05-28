# A composiçao é uma fomra mais forte de associaçao.
# Onde um objeto é parte de outro e nao pode existir de forma independente, ou seja, se o objeto for destruido, o outro também é destruido.
# Exemplo: Um carro tem um motor, o motor nao pode existir sem o carro,

import datetime
from Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()  # incializando a composiçao.

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["DEPOSITO", valor, "Data", datetime.datetime.today()]
        )

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, "Data", datetime.datetime.today()]
            )
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["TRANSFERENCIA", valor, "Data", datetime.datetime.today()]
            )
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"numero: {self.numero}\nsaldo: {self.saldo}")
