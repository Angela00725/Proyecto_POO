import re


def validar_rut(rut):
    rut_limpio = rut.replace(".", "").replace("-", "").strip().upper()
    if not re.fullmatch(r"\d{7,8}[0-9K]", rut_limpio):
        return False, "Formato de RUT inválido. Ejemplo: 12.345.678-5."

    cuerpo, digito_ingresado = rut_limpio[:-1], rut_limpio[-1]
    suma = 0
    multiplicador = 2
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1

    resultado = 11 - (suma % 11)
    digito_esperado = "0" if resultado == 11 else "K" if resultado == 10 else str(resultado)
    if digito_ingresado != digito_esperado:
        return False, "El dígito verificador del RUT es incorrecto."

    return True, f"{cuerpo}-{digito_ingresado}"
