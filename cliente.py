from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        try:
            if tipo == "movimientos":
                cliente = leerFichero(num)
            elif tipo == "guardado":
                cliente = cargarClienteGuardado(num)
            else:
                cliente = None

            if cliente is None:
                print("No se ha podido procesar el cliente solicitado.")
                return None

            return cliente

        except Exception as e:
            log.escribir("ERROR", f"Intento de consulta de cliente inexistente")
            print("Ocurrió un error al cargar el cliente.")
            return None


def leerFichero(numCliente):

    cliente = Cliente(numCliente)

    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()

            while linea:

                datos = linea.strip().split(";")

                cantidad = float(datos[0])
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

                linea = f.readline()

        # Guardamos el estado final del cliente
        cliente.guardar()


        print("Datos del cliente cargados correctamente")

        return cliente

    except FileNotFoundError:
        print("El usuario no tiene ninguna cuenta con el banco")
        log.escribir("ERROR", f"Error en la consulta del cliente : {numCliente}")
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
        log.escribir("ERROR", f"Intento de consulta de cliente inexistente : {numCliente}")
        return None