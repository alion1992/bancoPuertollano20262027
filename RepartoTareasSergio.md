# REPARTO DE TAREAS

Las tareas se repartirán entre los dos miembros de la pareja. Cada alumno será responsable de implementar y entregar sus propias ramas.

## Sergio

### Tarea 4 --- BUGFIX: Validar el tipo de log

**Rama:**
```text
bugfix/04-validar-tipo-log
```

La clase `Log` permite actualmente escribir cualquier tipo de mensaje. Modificarla para aceptar únicamente estos tipos:

```text
INFO
WARNING
ERROR
```

Si se recibe otro tipo, deberá registrarse como `INFO`. La aplicación no deberá detenerse.

---

### Tarea 5 --- BUGFIX: Movimiento con cantidad incorrecta

**Rama:**
```text
bugfix/05-cantidad-incorrecta
```

Un fichero podría contener una línea como:

```text
hola;Ingreso;Cuenta;
```

La conversión de `hola` a `float` produciría un error. Modificar el programa para que:

- Ignore ese movimiento.
- Continúe procesando el resto del fichero.
- Registre un `ERROR` indicando la línea problemática.

---

### Tarea 7 --- FEATURE: Contador de movimientos

**Rama:**
```text
feature/07-contador-movimientos
```

Durante la lectura del fichero, contar cuántos movimientos válidos se han procesado. Al finalizar, mostrar el total, por ejemplo:

```text
Movimientos procesados: 50
```

También se deberá registrar esta información en el log.

---

### Tarea 8 --- FEATURE: Consultar saldo total

**Rama:**
```text
feature/08-saldo-total
```

Añadir a la clase `Cliente` el método:

```python
def getSaldoTotal(self):
```

El método deberá devolver la suma del saldo de la cuenta y el saldo del depósito. En la opción de consulta también se mostrará:

```text
Saldo total: XXXX €
```

---

### Tarea 10 --- FEATURE: Mejorar el fichero de datos del cliente

**Rama:**
```text
feature/10-formato-datos-cliente
```

Modificar el fichero generado en `datosClientes/` para que cada dato aparezca en una línea:

```text
334433
1250.0
3500.0
```

Adaptar también la lectura del fichero para que la opción de consulta siga funcionando correctamente.

> Esta tarea afecta tanto a la escritura como a la lectura. Comprobad que un cliente puede guardarse y recuperarse correctamente.

---

## Coordinación

La tarea 3 debe integrarse con la tarea 2 para que el resumen aparezca después de una carga correcta. La tarea 10 cambia el formato de los datos del cliente, así que Sergio y Miguel deben coordinar ese cambio con las tareas de consulta y listado.
