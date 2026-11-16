from peewee import OperationalError

from auxiliares import (
    menu_superior,
    nombre_aplicacion,
    opcion_invalida,
    version_aplicacion,
)
from presentacion.presentacion_cliente import menu_clientes
from presentacion.presentacion_mesa import menu_mesas
from presentacion.presentacion_reserva import menu_reservas
from presentacion.presentacion_restaurante import menu_restaurantes
from presentacion.presentacion_horarioatencion import menu_horarios
from presentacion.presentacion_usuario import menu_usuarios


def menu_principal():
    separador = "=" * (len(nombre_aplicacion) + len(version_aplicacion) + 3)
    print(f"\n{nombre_aplicacion} - {version_aplicacion}")
    print(f"{separador}\n")

    while True:
        for clave, valor in menu_superior.items():
            print(f"[{clave}] - {valor}")

        opcion_usuario = input("\nIngrese su opción: ").strip()

        try:
            match opcion_usuario:
                case "1":
                    menu_restaurantes()
                case "2":
                    menu_reservas()
                case "3":
                    menu_mesas()
                case "4":
                    menu_clientes()
                case "5":
                    menu_usuarios()
                case "6":
                    menu_horarios()
                case "0":
                    print("\n¡Gracias por utilizar el sistema! Saliendo...")
                    break
                case _:
                    print(f"\n>> {opcion_invalida}")
        except OperationalError as error:
            print(f"\n>> Error al acceder a la base de datos: {error}")