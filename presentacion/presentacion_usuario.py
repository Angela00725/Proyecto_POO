from datetime import date

from maskpass import askpass
from prettytable import PrettyTable

from auxiliares.validar_rut import validar_rut
from auxiliares.validaciones import validar_contrasena, validar_correo
from negocio.negocio_usuario import (
    crear_usuario,
    eliminar_usuario_logico,
    modificar_usuario,
    obtener_usuarios,
)


def _solicitar_rut(opcional=False):
    while True:
        rut = input("RUT (Enter para conservar): " if opcional else "RUT: ").strip()
        if not rut and opcional:
            return rut
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


def _solicitar_fecha_nacimiento(opcional=False):
    while True:
        fecha = input(
            "Fecha de nacimiento (AAAA-MM-DD, opcional): "
            if opcional
            else "Fecha de nacimiento (AAAA-MM-DD): "
        ).strip()
        if not fecha and opcional:
            return fecha
        try:
            date.fromisoformat(fecha)
            return fecha
        except ValueError:
            print(">> Fecha inválida; use el formato AAAA-MM-DD.")


def _solicitar_genero(opcional=False):
    while True:
        genero = input(
            "Género [1 = Hombre, 2 = Mujer, 3 = Otro]: "
            if not opcional
            else "Nuevo género [1 = Hombre, 2 = Mujer, 3 = Otro; Enter para conservar]: "
        ).strip()
        if not genero and opcional:
            return None
        if genero in {"1", "2", "3"}:
            return int(genero)
        print(">> Ingrese 1, 2 o 3.")


def _solicitar_contrasena(opcional=False):
    while True:
        prompt = (
            "Nueva contraseña (Enter para conservar): "
            if opcional
            else "Contraseña: "
        )
        contrasena = askpass(prompt=prompt, mask="*")
        if not contrasena and opcional:
            return contrasena
        valida, mensaje = validar_contrasena(contrasena)
        if valida:
            return contrasena
        print(f">> {mensaje}")


def menu_usuarios():
    while True:
        print("\n==================================")
        print(" GESTIÓN DE USUARIOS ")
        print("==================================")
        print("1. Registrar usuario")
        print("2. Listar usuarios activos")
        print("3. Modificar usuario")
        print("4. Deshabilitar usuario")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()
        try:
            match opcion:
                case "1":
                    rut = _solicitar_rut()
                    nombre = ""
                    while not nombre:
                        nombre = input("Nombre: ").strip()
                        if not nombre:
                            print(">> El nombre es obligatorio.")
                    apellido = ""
                    while not apellido:
                        apellido = input("Apellido: ").strip()
                        if not apellido:
                            print(">> El apellido es obligatorio.")
                    correo = _solicitar_correo()
                    nacimiento = _solicitar_fecha_nacimiento(opcional=True)
                    genero = _solicitar_genero()
                    contrasena = _solicitar_contrasena()
                    _, mensaje = crear_usuario(
                        rut,
                        nombre,
                        apellido,
                        correo,
                        nacimiento,
                        genero,
                        contrasena,
                    )
                    print(f"\n>> {mensaje}")
                case "2":
                    mostrar_tabla_usuarios()
                case "3":
                    mostrar_tabla_usuarios()
                    id_usuario = int(input("ID del usuario a modificar: "))
                    print("(Presione Enter para conservar cada campo.)")
                    rut = _solicitar_rut(opcional=True)
                    nombre = input("Nuevo nombre: ")
                    apellido = input("Nuevo apellido: ")
                    correo = _solicitar_correo(opcional=True)
                    nacimiento = _solicitar_fecha_nacimiento(opcional=True)
                    genero = _solicitar_genero(opcional=True)
                    contrasena = _solicitar_contrasena(opcional=True)
                    _, mensaje = modificar_usuario(
                        id_usuario,
                        rut,
                        nombre,
                        apellido,
                        correo,
                        nacimiento,
                        genero,
                        contrasena,
                    )
                    print(f"\n>> {mensaje}")
                case "4":
                    mostrar_tabla_usuarios()
                    id_usuario = int(input("ID del usuario a deshabilitar: "))
                    _, mensaje = eliminar_usuario_logico(id_usuario)
                    print(f"\n>> {mensaje}")
                case "0":
                    break
                case _:
                    print("\n>> Opción no válida.")
        except ValueError:
            print("\n>> Ingrese valores numéricos válidos.")


def mostrar_tabla_usuarios():
    usuarios = obtener_usuarios()
    if not usuarios:
        print("\nNo hay usuarios activos registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "RUT",
        "Nombre",
        "Apellido",
        "Correo",
        "Nacimiento",
        "Género",
        "Incorporación",
    ]
    for usuario in usuarios:
        tabla.add_row(
            [
                usuario.id_usuario,
                usuario.rut or "N/I",
                usuario.nombre,
                usuario.apellido,
                usuario.correo,
                usuario.fecha_nacimiento or "N/I",
                {
                    1: "Hombre",
                    2: "Mujer",
                    3: "Otro",
                }.get(usuario.genero, f"Desconocido ({usuario.genero})"),
                usuario.fecha_incorporacion,
            ]
        )
    print(tabla)
