from datetime import datetime
import os


class Log:

    def __init__(self):
        fecha = datetime.now().strftime("%Y%m%d ")
        self.ruta = f"log/{fecha}-banco.log"

        if not os.path.exists("log"):
            os.mkdir("log")

    def escribir(self, tipo, mensaje):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tipos_validos = ["INFO", "WARNING", "ERROR"]

        # Normalizo el tipo a mayúsculas y, si no está permitido, lo dejo en INFO por defecto
        tipo_normalizado = str(tipo).upper() if tipo is not None else "INFO"
        if tipo_normalizado not in tipos_validos:
            tipo_normalizado = "INFO"

        with open(self.ruta, "a", encoding="utf-8") as fichero:
            fichero.write(f"[{fecha_hora}] [{tipo_normalizado}] {mensaje}\n")