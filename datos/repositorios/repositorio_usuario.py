from peewee import IntegrityError, OperationalError, fn

from datos.modelos.usuario import Usuario


def guardar_usuario(usuario_obj):
    try:
        usuario_obj.save()
        return True, "Usuario registrado exitosamente."
    except IntegrityError:
        return False, "El RUT o correo ya está registrado."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def buscar_usuario_por_rut(rut):
    rut_normalizado = rut.replace(".", "").replace("-", "").strip().upper()
    return Usuario.get_or_none(
        (
            fn.UPPER(fn.REPLACE(fn.REPLACE(Usuario.rut, ".", ""), "-", ""))
            == rut_normalizado
        )
        & (Usuario.habilitado == True)
    )


def buscar_usuario_por_correo(correo):
    return Usuario.get_or_none(
        (Usuario.correo == correo.strip()) & (Usuario.habilitado == True)
    )


def buscar_usuario_por_id(id_usuario):
    return Usuario.get_or_none(
        (Usuario.id_usuario == id_usuario) & (Usuario.habilitado == True)
    )


def listar_usuarios_activos():
    return list(
        Usuario.select()
        .where(Usuario.habilitado == True)
        .order_by(Usuario.id_usuario)
    )


def actualizar_usuario(usuario_obj):
    try:
        usuario_obj.save()
        return True, "Usuario actualizado exitosamente."
    except IntegrityError:
        return False, "El RUT o correo ya está registrado."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def eliminar_usuario_logico(id_usuario):
    usuario = buscar_usuario_por_id(id_usuario)
    if not usuario:
        return False, "Usuario no encontrado."

    usuario.habilitado = False
    return actualizar_usuario(usuario)
