from peewee import IntegrityError, OperationalError

from datos.modelos.horarioatencion import Horarioatencion


def guardar_horario(horario_obj):
    try:
        horario_obj.save()
        return True, "Horario registrado exitosamente."
    except IntegrityError:
        return False, "No fue posible registrar el horario por sus relaciones."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def listar_horarios_activos():
    return list(
        Horarioatencion.select()
        .where(Horarioatencion.habilitado == True)
        .order_by(Horarioatencion.id_horario)
    )


def buscar_horario_por_id(id_horario):
    return Horarioatencion.get_or_none(
        (Horarioatencion.id_horario == id_horario)
        & (Horarioatencion.habilitado == True)
    )


def actualizar_horario(horario_obj):
    try:
        horario_obj.save()
        return True, "Horario actualizado correctamente."
    except IntegrityError:
        return False, "No fue posible actualizar el horario por sus relaciones."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def eliminar_horario_logico(id_horario):
    horario = buscar_horario_por_id(id_horario)
    if not horario:
        return False, "Horario no encontrado."

    horario.habilitado = False
    return actualizar_horario(horario)
