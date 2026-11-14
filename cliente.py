from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        if tipo == "movimientos":
            return leerFichero(num)

        elif tipo == "guardado":
            return cargarClienteGuardado(num)


def leerFichero(numCliente):

    # Registro el inicio de la carga antes de abrir el fichero
    log.escribir("INFO", f"Inicio de la carga del cliente {numCliente}")
    cliente = Cliente(numCliente)

    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()

            while linea:

                datos = linea.strip().split(";")

                try:
                    cantidad = float(datos[0])
                except ValueError:
                    log.escribir("ERROR", f"Cantidad incorrecta en la línea: {linea.strip()}")
                    linea = f.readline()
                    continue

                operacion = datos[1]
                destino = datos[2]

                if destino == "Cuenta" and operacion == "Ingreso":
                    cliente.cuenta.ingresar(cantidad)

                elif destino == "Cuenta" and operacion == "Retirada":
                    cliente.cuenta.retirar(cantidad)

                elif destino == "Deposito" and operacion == "Ingreso":
                    cliente.deposito.ingresar(cantidad)

                elif destino == "Deposito" and operacion == "Retirada":
                    cliente.deposito.retirar(cantidad)

                else:
                    log.escribir("WARNING", f"Operación o destino desconocido en la línea: {linea.strip()}")

                linea = f.readline()

        # Guardamos el estado final del cliente
        cliente.guardar()

        # Confirmo en el log que el fichero se ha procesado sin problemas
        log.escribir("INFO", f"Cliente {numCliente} cargado correctamente")
        print("Datos del cliente cargados correctamente")

        # Muestro el resumen final sacando los datos directamente desde los getters de Cliente
        print(f"Cliente: {cliente.getNumero()}")
        print(f"Saldo cuenta: {cliente.getCuenta().getSaldo()} €")
        print(f"Saldo depósito: {cliente.getDeposito().getSaldo()} €")

        return cliente

    except FileNotFoundError:
        # Si no existe el archivo del cliente, dejo constancia como ERROR
        log.escribir("ERROR", f"Fichero de movimientos inexistente para el cliente {numCliente}")
        print("El usuario no tiene ninguna cuenta con el banco")
        return None


def cargarClienteGuardado(numCliente):

    try:
        with open(f"datosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()
            datos = linea.split(";")

            cliente = Cliente(datos[0])

            cliente.cuenta.saldo = float(datos[1])
            cliente.deposito.saldo = float(datos[2])

            return cliente

    except FileNotFoundError:
        print("Primero tienes que cargar los datos de este cliente")
        return None