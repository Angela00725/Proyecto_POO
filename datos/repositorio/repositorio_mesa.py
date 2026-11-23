from peewee import IntegrityError, OperationalError

from datos.modelos.mesas import Mesa


def guardar_mesa(mesa_obj):
    try:
        mesa_obj.save()
        return True, "Mesa registrada exitosamente."
    except IntegrityError:
        return False, "El número de mesa ya existe en este restaurante."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def listar_mesas_activas():
    return list(
        Mesa.select().where(Mesa.habilitado == True).order_by(Mesa.id_mesa)
    )


def buscar_mesa_por_id(id_mesa):
    return Mesa.get_or_none(
        (Mesa.id_mesa == id_mesa) & (Mesa.habilitado == True)
    )


def actualizar_mesa(mesa_obj):
    try:
        mesa_obj.save()
        return True, "Mesa actualizada correctamente."
    except IntegrityError:
        return False, "El número de mesa ya existe en este restaurante."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def eliminar_mesa_logico(id_mesa):
    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        return False, "Mesa no encontrada."

    mesa.habilitado = False
    return actualizar_mesa(mesa)
