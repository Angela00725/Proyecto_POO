from datos.modelos.reservas import Reserva


def guardar_reserva(reserva_obj):
    try:
        reserva_obj.save()
        return True, "¡Reserva realizada exitosamente!"
    except Exception as e:
        return False, f"Error al guardar la reserva: {e}"


def listar_reservas_activas():
    try:
        return list(Reserva.select().where(Reserva.habilitado == True))
    except Exception as e:
        print(f"Error al listar reservas: {e}")
        return []


def buscar_reserva_por_id(id_reserva):
    return Reserva.get_or_none(
        (Reserva.id_reserva == id_reserva) & (Reserva.habilitado == True)
    )


def actualizar_reserva(reserva_obj):
    try:
        reserva_obj.save()
        return True, "Reserva actualizada con éxito."
    except Exception as e:
        return False, f"Error al actualizar reserva: {e}"