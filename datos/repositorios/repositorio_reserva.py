from peewee import IntegrityError, OperationalError

from datos.modelos.reserva import (
    ESTADO_CANCELADA,
    ESTADO_COMPLETADA,
    ESTADO_RESERVADA,
    Reserva,
)


def guardar_reserva(reserva_obj):
    try:
        reserva_obj.save()
        return True, "Reserva realizada exitosamente."
    except IntegrityError:
        return False, "No fue posible registrar la reserva por sus relaciones."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def listar_reservas_activas():
    return list(
        Reserva.select()
        .where(
            (Reserva.habilitado == True)
        )
        .order_by(Reserva.fecha_reserva, Reserva.hora_reserva)
    )


def buscar_reserva_por_id(id_reserva):
    return Reserva.get_or_none(
        (Reserva.id_reserva == id_reserva) & (Reserva.habilitado == True)
    )


def actualizar_reserva(reserva_obj):
    try:
        reserva_obj.save()
        return True, "Reserva actualizada correctamente."
    except IntegrityError:
        return False, "No fue posible actualizar la reserva por sus relaciones."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def cancelar_reserva(id_reserva):
    reserva = buscar_reserva_por_id(id_reserva)
    if not reserva or reserva.estado != ESTADO_RESERVADA:
        return False, "Reserva activa no encontrada."

    reserva.estado = ESTADO_CANCELADA
    reserva.habilitado = False
    return actualizar_reserva(reserva)


def marcar_reserva_completada(id_reserva):
    reserva = buscar_reserva_por_id(id_reserva)
    if not reserva or reserva.estado != ESTADO_RESERVADA:
        return False, "Reserva activa no encontrada."

    reserva.estado = ESTADO_COMPLETADA
    return actualizar_reserva(reserva)
