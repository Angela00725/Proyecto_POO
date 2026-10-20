from prettytable import PrettyTable
from negocio.restaurante_negocio import (
    crear_restaurante,
    eliminar_restaurante_logico,
    listar_restaurantes_activos,
    modificar_restaurante,
    obtener_restaurantes,
)


def menu_restaurantes():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE RESTAURANTES ")
        print("==================================")
        print("1. Registrar restaurante")
        print("2. Listar restaurantes activos")
        print("3. Modificar restaurante")
        print("4. Eliminar restaurante (Borrado Lógico)")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n--- REGISTRAR RESTAURANTE ---")
                nombre = input("Nombre de la sucursal: ")
                direccion = input("Dirección: ")
                telefono = input("Teléfono (opcional): ")
                exito, mensaje = crear_restaurante(nombre, direccion, telefono)
                print(f"\n>> {mensaje}")
            case "2":
                mostrar_tabla_restaurantes()
            case "3":
                print("\n--- MODIFICAR RESTAURANTE ---")
                mostrar_tabla_restaurantes()
                try:
                    id_rest = int(input("\nIngrese el ID del restaurante a modificar: "))
                    print("(Presione Enter si no desea modificar un campo)")
                    n_nombre = input("Nuevo Nombre: ")
                    n_dir = input("Nueva Dirección: ")
                    n_tel = input("Nuevo Teléfono: ")
                    exito, mensaje = modificar_restaurante(id_rest, n_nombre, n_dir, n_tel)
                    print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: El ID debe ser un número entero.")
            case "4":
                print("\n--- ELIMINAR RESTAURANTE ---")
                mostrar_tabla_restaurantes()
                try:
                    id_rest = int(input("\nIngrese el ID del restaurante a deshabilitar: "))
                    confirmar = input(f"¿Confirma deshabilitar el restaurante ID {id_rest}? (s/n): ").lower()
                    if confirmar == 's':
                        exito, mensaje = eliminar_restaurante_logico(id_rest)
                        print(f"\n>> {mensaje}")
                except ValueError:
                    print("\n>> Error: El ID debe ser un número entero.")
            case "0":
                break
            case _:
                print("\n>> Opción no válida.")


def mostrar_tabla_restaurantes():
    lista = obtener_restaurantes()
    if not lista:
        print("\nNo hay restaurantes registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Dirección", "Teléfono"]
    for r in lista:
        tabla.add_row([r.id_restaurante, r.nombre, r.direccion, r.telefono or "N/I"])
    print(tabla)