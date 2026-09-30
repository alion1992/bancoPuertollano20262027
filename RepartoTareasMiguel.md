# REPARTO DE TAREAS

Las tareas se repartirán entre los dos miembros de la pareja. Cada alumno será responsable de implementar y entregar sus propias ramas.

## Miguel

### Tarea 1 --- BUGFIX: Consulta de cliente inexistente

**Rama:**
```text
bugfix/01-cliente-inexistente
```

Al consultar un cliente que no se ha cargado previamente, el programa puede intentar acceder a sus datos aunque el cliente sea `None`.

Corregir el problema para que:

- La aplicación no termine inesperadamente.
- Se muestre un mensaje adecuado.
- Se registre el intento en el log con nivel `ERROR`.

---

### Tarea 2 --- FEATURE: Registrar la carga de clientes

**Rama:**
```text
feature/02-log-carga-cliente
```

Añadir trazabilidad al proceso de carga de movimientos. El log deberá registrar:

- El inicio de la carga del cliente.
- La carga correcta del cliente.
- Si el fichero de movimientos no existe.

Utilizar los niveles `INFO` y `ERROR` según corresponda.

---

### Tarea 3 --- FEATURE: Mostrar resumen después de cargar

**Rama:**
```text
feature/03-resumen-carga
```

Después de procesar correctamente el fichero de movimientos, mostrar un resumen con este formato:

```text
Cliente: 334433
Saldo cuenta: XXXX €
Saldo depósito: XXXX €
```

La información debe obtenerse del objeto `Cliente`.

---

### Tarea 6 --- BUGFIX: Operación o destino desconocido

**Rama:**
```text
bugfix/06-movimiento-desconocido
```

Controlar movimientos con operaciones o destinos no reconocidos, por ejemplo:

```text
200;Transferencia;Cuenta;
```

o:

```text
200;Ingreso;Tarjeta;
```

Si la operación o el destino no se reconocen:

- El movimiento no se realizará.
- El programa continuará procesando el fichero.
- Se añadirá un `WARNING` al log.

---

### Tarea 9 --- FEATURE: Nueva opción «Listado de clientes»

**Rama:**
```text
feature/09-listado-clientes
```

Añadir al menú la opción:

```text
3) Listar clientes cargados
```

La opción deberá mostrar los números de los clientes cuyos datos estén guardados en la carpeta `datosClientes/`. Por ejemplo:

```text
Clientes cargados:

- 334433
- 443344
```

La opción «Salir» pasará a ser la opción **4**.

---

## Coordinación

La tarea 3 debe integrarse con la tarea 2 para que el resumen aparezca después de una carga correcta. La tarea 10 cambia el formato de los datos del cliente, así que Sergio y Miguel deben coordinar ese cambio con las tareas de consulta y listado.
