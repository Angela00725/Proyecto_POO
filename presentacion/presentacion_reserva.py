from prettytable import PrettyTable

from negocio.negocio_reserva import (
    cancelar_reserva,
    crear_reserva,
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
        print("2. Listar reservas activas")
        print("3. Cancelar reserva (Borrado Lógico)")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n--- CREAR RESERVA ---")
                mostrar_tabla_clientes()
                rut_cliente = input("\nIngrese el RUT del Cliente: ").strip()
                mostrar_tabla_mesas()
                try:
                    id_mesa = int(input("\nIngrese el ID de la Mesa seleccionada: "))
                    fecha = input("Fecha de reserva (AAAA-MM-DD): ").strip()
                    hora = input("Hora de reserva (HH:MM): ").strip()
                    cant = int(input("Cantidad de asistentes: "))
                    exito, mensaje = crear_reserva(rut_cliente, id_mesa, fecha, hora, cant)
                    print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: La mesa y cantidad deben ser valores numéricos.")
            case "2":
                mostrar_tabla_reservas()
            case "3":
                print("\n--- CANCELAR RESERVA ---")
                mostrar_tabla_reservas()
                try:
                    id_res = int(input("\nIngrese el ID de la reserva a cancelar: "))
                    mensaje = cancelar_reserva(id_res)
                    print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: El ID debe ser un número entero.")
            case "0":
                break
            case _:
                print("\n>> Opción no válida.")


def mostrar_tabla_reservas():
    lista = obtener_reservas()
    if not lista:
        print("\nNo hay reservas registradas.")
        return

    tabla = PrettyTable()
    tabla.field_names = [
        "ID Reserva",
        "Cliente",
        "Restaurante",
        "N° Mesa",
        "Fecha",
        "Hora",
        "Asistentes",
        "Estado",
    ]
    for r in lista:
        tabla.add_row([
            r.id_reserva,
            r.id_cliente.nombre_apellido,
            r.id_mesa.id_restaurante.nombre,
            r.id_mesa.numero_mesa,
            r.fecha_reserva,
            r.hora_reserva,
            r.cantidad_personas,
            r.estado,
        ])
    print(tabla)