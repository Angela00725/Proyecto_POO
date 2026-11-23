from datetime import date

from auxiliares.validaciones import generar_hash, validar_contrasena, validar_correo
from auxiliares.validar_rut import validar_rut
from datos.modelos.usuario import Usuario
from datos.repositorio.repositorio_usuario import (
    actualizar_usuario,
    buscar_usuario_por_id,
    guardar_usuario,
    listar_usuarios_activos,
)


def crear_usuario(
    rut,
    nombre,
    apellido,
    correo,
    fecha_nacimiento,
    genero,
    contrasena,
):
    if not nombre.strip() or not apellido.strip():
        return False, "El nombre y el apellido son obligatorios."

    correo_valido, correo_resultado = validar_correo(correo)
    if not correo_valido:
        return False, correo_resultado

    if not rut.strip():
        return False, "El RUT es obligatorio."
    rut_valido, rut_resultado = validar_rut(rut)
    if not rut_valido:
        return False, rut_resultado
    rut_formateado = rut_resultado

    contrasena_valida, mensaje = validar_contrasena(contrasena)
    if not contrasena_valida:
        return False, mensaje

    nacimiento = None
    if fecha_nacimiento.strip():
        try:
            nacimiento = date.fromisoformat(fecha_nacimiento.strip())
        except ValueError:
            return False, "La fecha de nacimiento debe tener formato AAAA-MM-DD."

    usuario = Usuario(
        rut=rut_formateado,
        nombre=nombre.strip(),
        apellido=apellido.strip(),
        correo=correo_resultado,
        fecha_nacimiento=nacimiento,
        genero=genero,
        fecha_incorporacion=date.today(),
        habilitado=True,
        password=generar_hash(contrasena),
    )
    return guardar_usuario(usuario)


def obtener_usuarios():
    return listar_usuarios_activos()


def modificar_usuario(
    id_usuario,
    rut,
    nombre,
    apellido,
    correo,
    fecha_nacimiento,
    genero,
    contrasena,
):
    usuario = buscar_usuario_por_id(id_usuario)
    if not usuario:
        return False, "Usuario no encontrado."

    if rut.strip():
        rut_valido, rut_resultado = validar_rut(rut)
        if not rut_valido:
            return False, rut_resultado
        usuario.rut = rut_resultado
    if nombre.strip():
        usuario.nombre = nombre.strip()
    if apellido.strip():
        usuario.apellido = apellido.strip()
    if correo.strip():
        correo_valido, correo_resultado = validar_correo(correo)
        if not correo_valido:
            return False, correo_resultado
        usuario.correo = correo_resultado
    if fecha_nacimiento.strip():
        try:
            usuario.fecha_nacimiento = date.fromisoformat(fecha_nacimiento.strip())
        except ValueError:
            return False, "La fecha de nacimiento debe tener formato AAAA-MM-DD."
    if genero is not None:
        usuario.genero = genero
    if contrasena:
        contrasena_valida, mensaje = validar_contrasena(contrasena)
        if not contrasena_valida:
            return False, mensaje
        usuario.password = generar_hash(contrasena)

    return actualizar_usuario(usuario)


def eliminar_usuario_logico(id_usuario):
    usuario = buscar_usuario_por_id(id_usuario)
    if not usuario:
        return False, "Usuario no encontrado."

    usuario.habilitado = False
    return actualizar_usuario(usuario)
