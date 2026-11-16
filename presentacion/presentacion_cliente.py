from prettytable import PrettyTable

from negocio.negocio_cliente import (
    crear_cliente,
    eliminar_cliente_logico,
    modificar_cliente,
    obtener_clientes,
)
from auxiliares.validar_rut import validar_rut
from auxiliares.validaciones import validar_correo


def _solicitar_rut():
    while True:
        rut = input("RUT: ").strip()
        rut_valido, mensaje = validar_rut(rut)
        if rut_valido:
            return rut
        print(f"\n>> {mensaje} Intente nuevamente.")


def _solicitar_correo(opcional=False):
    while True:
        correo = input("Correo (opcional): " if opcional else "Correo: ").strip()
        if not correo and opcional:
            return correo
        correo_valido, resultado = validar_correo(correo)
        if correo_valido:
            return resultado
        print(f"\n>> {resultado} Intente nuevamente.")


def menu_clientes():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE CLIENTES ")
        print("==================================")
        print("1. Registrar nuevo cliente")
        print("2. Listar clientes activos")
        print("3. Modificar cliente por RUT")
        print("4. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n--- REGISTRAR CLIENTE ---")
                rut = _solicitar_rut()
                nombre = ""
                while not nombre:
                    nombre = input("Nombre y Apellido: ").strip()
                    if not nombre:
                        print("\n>> El nombre es obligatorio.")
                correo = _solicitar_correo(opcional=True)
                telefono = input("Teléfono (opcional): ")
                _, mensaje = crear_cliente(rut, nombre, correo, telefono)
                print(f"\n>> {mensaje}")
            case "2":
                mostrar_tabla_clientes()
            case "3":
                print("\n--- MODIFICAR CLIENTE ---")
                mostrar_tabla_clientes()
                rut = _solicitar_rut()
                print("(Presione Enter si no desea modificar un campo)")
                n_nombre = input("Nuevo Nombre: ")
                n_correo = _solicitar_correo(opcional=True)
                n_telefono = input("Nuevo Teléfono: ")
                _, mensaje = modificar_cliente(rut, n_nombre, n_correo, n_telefono)
                print(f"\n>> {mensaje}")
            case "4":
                print("\n--- ELIMINAR CLIENTE ---")
                mostrar_tabla_clientes()
                rut = input("\nIngrese el RUT del cliente a deshabilitar: ").strip()
                confirmar = input(f"¿Confirma deshabilitar al cliente con RUT {rut}? (s/n): ").lower()
                if confirmar == "s":
                    _, mensaje = eliminar_cliente_logico(rut)
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