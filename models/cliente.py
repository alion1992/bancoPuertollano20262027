import os

class Cliente:

    def __init__(self, numero):
        self.numero = numero
        self.cuenta = CuentaBancaria()
        self.deposito = Deposito()

    def getNumero(self):
        return self.numero

    def getCuenta(self):
        return self.cuenta

    def getDeposito(self):
        return self.deposito

    def guardar(self):
        if not os.path.exists("datosClientes"):
            os.mkdir("datosClientes")

        with open(f"datosClientes/{self.numero}.txt", "w") as f:
            f.write(
                f"{self.numero};"
                f"{self.cuenta.getSaldo()};"
                f"{self.deposito.getSaldo()}"
            )