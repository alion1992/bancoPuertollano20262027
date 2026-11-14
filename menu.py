from cliente import cargarCliente
from logs import Log
from  pathlib import Path

log = Log()

def menu():

    while True:

        print("1) Cargar Datos Cliente")
        print("2) Consultar cuenta Deposito")
        print("3) Listar clientes cargados")
        print("4) Salir")

        opt = input("Introduce la opción deseada: ")

        if opt == "1":
            cargarCliente("movimientos")


        elif opt == "2":

            cliente = cargarCliente("guardado")

            # Compruebo primero si el cliente existe para evitar el fallo al leer cliente.numero

            if cliente is not None:

                log.escribir("INFO", f"CONSULTA DATOS CLIENTE CON NÚMERO: {cliente.numero}")

                print(f"Cliente: {cliente.numero}")

                print(f"Saldo cuenta: {cliente.cuenta.saldo} €")

                print(f"Saldo depósito: {cliente.deposito.saldo} €")
                print(f"Saldo total: {cliente.getSaldoTotal()} €")

            else:

                # Si devuelve None, registro el error en el log y aviso por pantalla

                log.escribir("ERROR", "Intento de consulta de un cliente no cargado o inexistente")

                print("Error: No se puede consultar porque el cliente no existe o no ha sido cargado previamente.")
        elif opt == "3":
            carpeta = Path("datosClientes")
            if not carpeta.exists():
                print("No existe la carpeta datosClientes.")
            elif not any(carpeta.iterdir()):
                print("No hay clientes cargados todavía.")
            else:
                print("Clientes cargados:\n")

                for archivo in carpeta.iterdir():
                    if archivo.suffix == ".txt":
                        print("- " + archivo.stem)

        elif opt == "4":
            log.escribir(
                "INFO",
                "FIN EJECUCIÓN"
            )
            print("Hasta pronto")
            break

        else:
            log.escribir(
                "WARNING",
                "SE HA INTRODUCIDO UNA OPCION EN EL MENÚ NO RECONOCIDA"
            )
            print("No se ha seleccionado ninguna opción correcta")