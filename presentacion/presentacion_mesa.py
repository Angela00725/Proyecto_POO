from prettytable import PrettyTable

from negocio.mesa_negocio import (
    crear_mesa,
    eliminar_mesa_logico,
    obtener_mesas,
)
from presentacion.restaurante_presentacion import mostrar_tabla_restaurantes


def menu_mesas():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE MESAS ")
        print("==================================")
        print("1. Registrar nueva mesa")
        print("2. Listar todas las mesas")
        print("3. Eliminar mesa (Borrado Lógico)")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n--- REGISTRAR MESA ---")
                mostrar_tabla_restaurantes()
                try:
                    id_rest = int(input("\nIngrese el ID del Restaurante donde está la mesa: "))
                    num_mesa = int(input("Número de Mesa: "))
                    capacidad = int(input("Capacidad de personas: "))
                    exito, mensaje = crear_mesa(id_rest, num_mesa, capacidad)
                    print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: Debe ingresar números válidos.")
            case "2":
                mostrar_tabla_mesas()
            case "3":
                print("\n--- ELIMINAR MESA ---")
                mostrar_tabla_mesas()
                try:
                    id_m = int(input("\nIngrese el ID de la mesa a deshabilitar: "))
                    exito, mensaje = eliminar_mesa_logico(id_m)
                    print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: Debe ingresar un número entero.")
            case "0":
                break
            case _:
                print("\n>> Opción no válida.")


def mostrar_tabla_mesas():
    lista = obtener_mesas()
    if not lista:
        print("\nNo hay mesas registradas.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID Mesa", "Restaurante", "N° Mesa", "Capacidad (Personas)"]
    for m in lista:
        tabla.add_row([m.id_mesa, m.id_restaurante.nombre, m.numero_mesa, m.capacidad_personas])
    print(tabla)