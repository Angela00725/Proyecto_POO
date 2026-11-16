from prettytable import PrettyTable

from datos.modelos.reserva import (
    ESTADO_CANCELADA,
    ESTADO_COMPLETADA,
    ESTADO_RESERVADA,
)
from negocio.negocio_reserva import (
    cancelar_reserva,
    crear_reserva,
    marcar_reserva_completada,
    modificar_reserva,
    obtener_reservas,
)
from presentacion.presentacion_cliente import mostrar_tabla_clientes
from presentacion.presentacion_mesa import mostrar_tabla_mesas


def menu_reservas():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE RESERVAS ")
        print("==================================")
        print("1. Crear nueva reserva")
        print("2. Listar reservas")
        print("3. Modificar reserva")
        print("4. Cancelar reserva")
        print("5. Marcar reserva como completada")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()
        try:
            match opcion:
                case "1":
                    mostrar_tabla_clientes()
                    rut_cliente = input("RUT del cliente: ").strip()
                    mostrar_tabla_mesas()
                    id_mesa = int(input("ID de la mesa: "))
                    fecha = input("Fecha (AAAA-MM-DD): ").strip()
                    hora = input("Hora (HH:MM): ").strip()
                    cantidad = int(input("Cantidad de asistentes: "))
                    _, mensaje = crear_reserva(
                        rut_cliente, id_mesa, fecha, hora, cantidad
                    )
                    print(f"\n>> {mensaje}")
                case "2":
                    mostrar_tabla_reservas()
                case "3":
                    mostrar_tabla_reservas()
                    id_reserva = int(input("ID de la reserva a modificar: "))
                    fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
                    hora = input("Nueva hora (HH:MM): ").strip()
                    cantidad = int(input("Nueva cantidad de asistentes: "))
                    _, mensaje = modificar_reserva(
                        id_reserva, fecha, hora, cantidad
                    )
                    print(f"\n>> {mensaje}")
                case "4":
                    mostrar_tabla_reservas()
                    id_reserva = int(input("ID de la reserva a cancelar: "))
                    _, mensaje = cancelar_reserva(id_reserva)
                    print(f"\n>> {mensaje}")
                case "5":
                    mostrar_tabla_reservas()
                    id_reserva = int(input("ID de la reserva completada: "))
                    _, mensaje = marcar_reserva_completada(id_reserva)
                    print(f"\n>> {mensaje}")
                case "0":
                    break
                case _:
                    print("\n>> Opción no válida.")
        except ValueError:
            print("\n>> Ingrese valores numéricos válidos.")


def mostrar_tabla_reservas():
    reservas = obtener_reservas()
    if not reservas:
        print("\nNo hay reservas registradas.")
        return

    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "Cliente",
        "Restaurante",
        "Mesa",
        "Fecha",
        "Hora",
        "Asistentes",
        "Estado",
    ]
    for reserva in reservas:
        tabla.add_row(
            [
                reserva.id_reserva,
                reserva.id_cliente.nombre_apellido,
                reserva.id_restaurante.nombre,
                reserva.id_mesa.numero_mesa,
                reserva.fecha_reserva,
                reserva.hora_reserva,
                reserva.cantidad_personas,
                {
                    ESTADO_RESERVADA: "Reservada",
                    ESTADO_CANCELADA: "Cancelada",
                    ESTADO_COMPLETADA: "Completada",
                }.get(reserva.estado, f"Estado desconocido ({reserva.estado})"),
            ]
        )
    print(tabla)
