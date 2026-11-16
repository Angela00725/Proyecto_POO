from prettytable import PrettyTable

from negocio.negocio_horarioatencion import (
    crear_horario,
    eliminar_horario_logico,
    modificar_horario,
    obtener_horarios,
)
from presentacion.presentacion_restaurante import mostrar_tabla_restaurantes


def menu_horarios():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE HORARIOS DE ATENCIÓN ")
        print("==================================")
        print("1. Registrar horario")
        print("2. Listar horarios activos")
        print("3. Modificar horario")
        print("4. Eliminar horario")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()
        try:
            match opcion:
                case "1":
                    mostrar_tabla_restaurantes()
                    id_restaurante = int(input("ID del restaurante: "))
                    dia = input("Día o rango de atención: ")
                    apertura = input("Hora de apertura (HH:MM): ")
                    cierre = input("Hora de cierre (HH:MM): ")
                    _, mensaje = crear_horario(
                        id_restaurante, dia, apertura, cierre
                    )
                    print(f"\n>> {mensaje}")
                case "2":
                    mostrar_tabla_horarios()
                case "3":
                    mostrar_tabla_horarios()
                    id_horario = int(input("ID del horario a modificar: "))
                    mostrar_tabla_restaurantes()
                    id_restaurante = int(input("Nuevo ID del restaurante: "))
                    dia = input("Nuevo día o rango: ")
                    apertura = input("Nueva hora de apertura (HH:MM): ")
                    cierre = input("Nueva hora de cierre (HH:MM): ")
                    _, mensaje = modificar_horario(
                        id_horario,
                        id_restaurante,
                        dia,
                        apertura,
                        cierre,
                    )
                    print(f"\n>> {mensaje}")
                case "4":
                    mostrar_tabla_horarios()
                    id_horario = int(input("ID del horario a eliminar: "))
                    _, mensaje = eliminar_horario_logico(id_horario)
                    print(f"\n>> {mensaje}")
                case "0":
                    break
                case _:
                    print("\n>> Opción no válida.")
        except ValueError:
            print("\n>> Ingrese valores numéricos válidos.")


def mostrar_tabla_horarios():
    horarios = obtener_horarios()
    if not horarios:
        print("\nNo hay horarios activos registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "Restaurante",
        "Día",
        "Apertura",
        "Cierre",
    ]
    for horario in horarios:
        tabla.add_row(
            [
                horario.id_horario,
                horario.id_restaurante.nombre,
                horario.dia_semana,
                horario.hora_apertura,
                horario.hora_cierre,
            ]
        )
    print(tabla)
