# Proyecto_POO
Proyecto de desarrollo en POO

### 1. Módulo `Cliente` (Plantilla CRUD Completa)

#### A. Capa de Datos (`datos/repositorios/cliente_repositorio.py`)
```python
from peewee import IntegrityError, OperationalError
from datos.modelos.cliente import Cliente

def guardar_cliente(cliente_obj):
    """Guarda un nuevo cliente en MySQL mediante Peewee"""
    try:
        cliente_obj.save()
        return True, "Cliente registrado con éxito."
    except IntegrityError:
        return False, "Error: El RUT ingresado ya existe en la base de datos."
    except OperationalError as e:
        return False, f"Error de conexión con la base de datos: {e}"

def listar_clientes_activos():
    """Trae solo los clientes con borrado lógico activo (habilitado = True)"""
    try:
        return list(Cliente.select().where(Cliente.habilitado == True))
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
        return []

def buscar_cliente_por_id(id_cliente):
    """Busca un cliente por su ID primario"""
    return Cliente.get_or_none((Cliente.id_cliente == id_cliente) & (Cliente.habilitado == True))

def actualizar_cliente(cliente_obj):
    """Guarda los cambios de un cliente modificado"""
    try:
        cliente_obj.save() # Peewee ejecuta UPDATE automáticamente al haber cambios
        return True, "Cliente actualizado correctamente."
    except Exception as e:
        return False, f"Error al actualizar: {e}"
```

#### B. Capa de Negocio (`negocio/cliente_negocio.py`)
```python
from datos.modelos.cliente import Cliente
from datos.repositorios.cliente_repositorio import (
    repo_guardar_cliente,
    repo_listar_clientes_activos,
    repo_buscar_cliente_por_id,
    repo_actualizar_cliente
)

def crear_cliente(rut, nombre_apellido, correo, telefono):
    # Validaciones básicas de negocio
    if not rut.strip() or not nombre_apellido.strip():
        return False, "El RUT y el Nombre son obligatorios."
    
    # Instanciación de la clase (Modelo ORM)
    nuevo_cliente = Cliente(
        rut=rut.strip(),
        nombre_apellido=nombre_apellido.strip(),
        correo=correo.strip() if correo.strip() else None,
        telefono=telefono.strip() if telefono.strip() else None,
        habilitado=True # Por defecto nace activo
    )
    return repo_guardar_cliente(nuevo_cliente)

def obtener_clientes():
    return repo_listar_clientes_activos()

def modificar_cliente(id_cliente, nuevo_nombre, nuevo_correo, nuevo_telefono):
    cliente = repo_buscar_cliente_por_id(id_cliente)
    if not cliente:
        return False, "No se encontró ningún cliente activo con ese ID."
    
    # Si el usuario presiona Enter (cadena vacía), se conserva el valor actual
    if nuevo_nombre.strip():
        cliente.nombre_apellido = nuevo_nombre.strip()
    if nuevo_correo.strip():
        cliente.correo = nuevo_correo.strip()
    if nuevo_telefono.strip():
        cliente.telefono = nuevo_telefono.strip()
        
    return repo_actualizar_cliente(cliente)

def eliminar_cliente_logico(id_cliente):
    cliente = repo_buscar_cliente_por_id(id_cliente)
    if not cliente:
        return False, "No se encontró ningún cliente activo con ese ID."
    
    # Borrado Lógico: Cambiar estado a deshabilitado
    cliente.habilitado = False
    return repo_actualizar_cliente(cliente)
```

#### C. Capa de Presentación (`presentacion/cliente_presentacion.py`)
```python
from prettytable import PrettyTable
from negocio.cliente_negocio import (
    crear_cliente,
    obtener_clientes,
    modificar_cliente,
    eliminar_cliente_logico
)

def menu_clientes():
    while True:
        print("\n==================================")
        print("      GESTIÓN DE CLIENTES         ")
        print("==================================")
        print(" Registrar nuevo cliente")
        print(" Listar clientes activos")
        print(" Modificar datos de cliente")
        print(" Eliminar cliente (Borrado lógico)")
        print(" Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        match opcion:
            case "1":
                print("\n--- REGISTRAR CLIENTE ---")
                rut = input("RUT: ")
                nombre = input("Nombre y Apellido: ")
                correo = input("Correo (opcional): ")
                telefono = input("Teléfono (opcional): ")
                
                exito, mensaje = crear_cliente(rut, nombre, correo, telefono)
                print(f"\n>> {mensaje}")
                
            case "2":
                mostrar_tabla_clientes()
                
            case "3":
                print("\n--- MODIFICAR CLIENTE ---")
                mostrar_tabla_clientes()
                try:
                    id_cliente = int(input("\nIngrese el ID del cliente a modificar: "))
                    print("(Deje el campo en blanco y presione Enter si no desea modificarlo)")
                    n_nombre = input("Nuevo Nombre: ")
                    n_correo = input("Nuevo Correo: ")
                    n_telefono = input("Nuevo Teléfono: ")
                    
                    exito, mensaje = modificar_cliente(id_cliente, n_nombre, n_correo, n_telefono)
                    print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: El ID debe ser un número entero.")
                    
            case "4":
                print("\n--- ELIMINAR CLIENTE ---")
                mostrar_tabla_clientes()
                try:
                    id_cliente = int(input("\nIngrese el ID del cliente a eliminar: "))
                    confirmar = input("¿Está seguro de deshabilitar este cliente? (s/n): ").lower()
                    if confirmar == 's':
                        exito, mensaje = eliminar_cliente_logico(id_cliente)
                        print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: El ID debe ser un número entero.")
                    
            case "0":
                break
            case _:
                print("\n>> Opción no válida.")

def mostrar_tabla_clientes():
    lista = obtener_clientes()
    if not lista:
        print("\nNo hay clientes registrados o activos.")
        return
    
    tabla = PrettyTable()
    tabla.field_names = ["ID", "RUT", "Nombre y Apellido", "Correo", "Teléfono"]
    for c in lista:
        tabla.add_row([c.id_cliente, c.rut, c.nombre_apellido, c.correo or "N/I", c.telefono or "N/I"])
    print(tabla)
```

---

### 2. Módulo `Reserva` (Relación entre Cliente y Mesa)

#### Capa de Negocio de Reserva (`negocio/reserva_negocio.py`)
```python
from datos.modelos.reserva import Reserva
from datos.modelos.cliente import Cliente
from datos.modelos.mesa import Mesa

def crear_reserva(id_cliente, id_mesa, fecha_reserva, hora_reserva, cantidad_personas):
    # Validar que existan el cliente y la mesa
    cliente = Cliente.get_or_none((Cliente.id_cliente == id_cliente) & (Cliente.habilitado == True))
    if not cliente:
        return False, "El cliente seleccionado no existe o está deshabilitado."
        
    mesa = Mesa.get_or_none((Mesa.id_mesa == id_mesa) & (Mesa.habilitada == True))
    if not mesa:
        return False, "La mesa seleccionada no existe o no está habilitada."
        
    nueva_reserva = Reserva(
        id_cliente=cliente,
        id_mesa=mesa,
        fecha_reserva=fecha_reserva,
        hora_reserva=hora_reserva,
        cantidad_personas=cantidad_personas,
        estado="Reservada",
        habilitado=True
    )
    
    try:
        nueva_reserva.save()
        return True, "¡Reserva realizada exitosamente!"
    except Exception as e:
        return False, f"Error al guardar la reserva: {e}"
```

---

### 3. Punto de Entrada (`app.py`)

```python
from presentacion.cliente_presentacion import menu_clientes
# Importar los menús de presentación que armen tus compañeros (restaurante_presentacion, etc.)

def main():
    while True:
        print("\n==========================================")
        print("  SISTEMA DE RESERVAS RESTAURANTE POO     ")
        print("==========================================")
        print(" Gestión de Clientes")
        print(" Gestión de Restaurantes")
        print(" Gestión de Mesas")
        print(" Gestión de Reservas")
        print(" Salir del Sistema")
        
        opcion = input("\nIngrese una opción: ").strip()
        
        match opcion:
            case "1":
                menu_clientes()
            case "2":
                print("\n[En desarrollo por Integrante 2]")
            case "3":
                print("\n[En desarrollo por Integrante 2]")
            case "4":
                print("\n[En desarrollo por Integrante 3]")
            case "0":
                print("\nSaliendo del sistema...")
                break
            case _:
                print("\nOpción inválida.")

if __name__ == "__main__":
    main()
```

---

### Pasos recomendados para tu equipo hoy:
1. Pasa este código de `Cliente` a tus carpetas y pruébalo ejecutando `python app.py`.
2. Comparte la estructura con tus compañeros para que repliquen los archivos de `Restaurante` y `Mesa` cambiando únicamente los atributos del modelo.
3. Asegúrense de subir al repositorio de GitHub el archivo `.env` y el script `.sql` de la base de datos como requirió el profesor para la evaluación.
