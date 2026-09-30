import os


class Deposito:

    def __init__(self):
        self.saldo = 0

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def getSaldo(self):
        return self.saldo


