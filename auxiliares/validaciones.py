import re

import bcrypt


def validar_correo(correo):
    correo = correo.strip().lower()
    if not re.fullmatch(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", correo):
        return False, "Formato de correo inválido."
    return True, correo


def validar_contrasena(contrasena):
    errores = []
    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres.")
    if not any(caracter.isdigit() for caracter in contrasena):
        errores.append("Debe incluir al menos un número.")
    if not any(caracter.islower() for caracter in contrasena):
        errores.append("Debe incluir al menos una minúscula.")
    if not any(caracter.isupper() for caracter in contrasena):
        errores.append("Debe incluir al menos una mayúscula.")
    if not any(caracter in "@$#!*&" for caracter in contrasena):
        errores.append("Debe incluir un carácter especial: @, $, #, !, * o &.")
    if len(contrasena.encode("utf-8")) > 72:
        errores.append("No puede superar los 72 bytes.")
    if errores:
        return False, "La contraseña no cumple los requisitos: " + " ".join(errores)
    return True, "Contraseña válida."


def generar_hash(texto):
    return bcrypt.hashpw(
        texto.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")