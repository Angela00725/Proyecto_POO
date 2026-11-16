from prettytable import PrettyTable

from negocio.negocio_mesa import (
    crear_mesa,
    eliminar_mesa_logico,
    modificar_mesa,
    obtener_mesas,
)
from presentacion.presentacion_restaurante import mostrar_tabla_restaurantes


def menu_mesas():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE MESAS ")
        print("==================================")
        print("1. Registrar nueva mesa")
        print("2. Listar mesas activas")
        print("3. Modificar mesa")
        print("4. Eliminar mesa")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()
        try:
            match opcion:
                case "1":
                    mostrar_tabla_restaurantes()
                    id_restaurante = int(input("ID del restaurante: "))
                    numero = int(input("Número de mesa: "))
                    capacidad = int(input("Capacidad de personas: "))
                    ubicacion = input("Ubicación (opcional): ")
                    _, mensaje = crear_mesa(
                        id_restaurante, numero, capacidad, ubicacion
                    )
                    print(f"\n>> {mensaje}")
                case "2":
                    mostrar_tabla_mesas()
                case "3":
                    mostrar_tabla_mesas()
                    id_mesa = int(input("ID de la mesa a modificar: "))
                    mostrar_tabla_restaurantes()
                    id_restaurante = int(input("Nuevo ID del restaurante: "))
                    numero = int(input("Nuevo número de mesa: "))
                    capacidad = int(input("Nueva capacidad: "))
                    ubicacion = input("Nueva ubicación (opcional): ")
                    _, mensaje = modificar_mesa(
                        id_mesa,
                        id_restaurante,
                        numero,
                        capacidad,
                        ubicacion,
                    )
                    print(f"\n>> {mensaje}")
                case "4":
                    mostrar_tabla_mesas()
                    id_mesa = int(input("ID de la mesa a deshabilitar: "))
                    _, mensaje = eliminar_mesa_logico(id_mesa)
                    print(f"\n>> {mensaje}")
                case "0":
                    break
                case _:
                    print("\n>> Opción no válida.")
        except ValueError:
            print("\n>> Ingrese valores numéricos válidos.")


def mostrar_tabla_mesas():
    mesas = obtener_mesas()
    if not mesas:
        print("\nNo hay mesas activas registradas.")
        return

    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "Restaurante",
        "N° Mesa",
        "Capacidad",
        "Ubicación",
    ]
    for mesa in mesas:
        tabla.add_row(
            [
                mesa.id_mesa,
                mesa.id_restaurante.nombre,
                mesa.numero_mesa,
                mesa.capacidad_personas,
                mesa.ubicacion or "N/I",
            ]
        )
    print(tabla)
