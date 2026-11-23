import bcrypt

from auxiliares.validaciones import validar_correo
from datos.repositorio.repositorio_usuario import buscar_usuario_por_correo


def login_usuario(correo, contrasena):
    correo_valido, correo_resultado = validar_correo(correo)
    if not correo_valido:
        return None, correo_resultado

    usuario = buscar_usuario_por_correo(correo_resultado)
    if not usuario:
        return None, "Usuario no encontrado."

    try:
        coincide = bcrypt.checkpw(
            contrasena.encode("utf-8"),
            usuario.password.encode("utf-8"),
        )
    except (AttributeError, ValueError):
        coincide = False

    if not coincide:
        return None, "Contraseña incorrecta."

    return usuario, "Inicio de sesión exitoso."