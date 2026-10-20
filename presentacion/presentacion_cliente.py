from prettytable import PrettyTable

from negocio.negocio_cliente import (
    crear_cliente,
    eliminar_cliente_logico,
    modificar_cliente,
    obtener_clientes,
)


def menu_clientes():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE CLIENTES ")
        print("==================================")
        print("1. Registrar nuevo cliente")
        print("2. Listar clientes activos")
        print("3. Modificar cliente por RUT")
        print("4. Eliminar cliente (Borrado Lógico)")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n--- REGISTRAR CLIENTE ---")
                rut = input("RUT: ")
                nombre = input("Nombre y Apellido: ")
                correo = input("Correo (opcional): ")
                telefono = input("Teléfono (opcional): ")
                mensaje = crear_cliente(rut, nombre, correo, telefono)
                print(f"\n>> {mensaje}")
            case "2":
                mostrar_tabla_clientes()
            case "3":
                print("\n--- MODIFICAR CLIENTE ---")
                mostrar_tabla_clientes()
                rut = input("\nIngrese el RUT del cliente a modificar: ").strip()
                print("(Presione Enter si no desea modificar un campo)")
                n_nombre = input("Nuevo Nombre: ")
                n_correo = input("Nuevo Correo: ")
                n_telefono = input("Nuevo Teléfono: ")
                mensaje = modificar_cliente(rut, n_nombre, n_correo, n_telefono)
                print(f"\n>> {mensaje}")
            case "4":
                print("\n--- ELIMINAR CLIENTE ---")
                mostrar_tabla_clientes()
                rut = input("\nIngrese el RUT del cliente a deshabilitar: ").strip()
                confirmar = input(f"¿Confirma deshabilitar al cliente con RUT {rut}? (s/n): ").lower()
                if confirmar == "s":
                    mensaje = eliminar_cliente_logico(rut)
                    print(f"\n>> {mensaje}")
            case "0":
                break
            case _:
                print("\n>> Opción no válida.")


def mostrar_tabla_clientes():
    lista = obtener_clientes()
    if not lista:
        print("\nNo hay clientes activos registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["RUT", "Nombre y Apellido", "Correo", "Teléfono"]
    for c in lista:
        tabla.add_row([
            c.rut,
            c.nombre_apellido,
            c.correo or "N/I",
            c.telefono or "N/I",
        ])
    print(tabla)