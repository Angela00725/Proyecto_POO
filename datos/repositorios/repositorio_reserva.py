from datos.modelos.reserva import Reserva


def guardar_reserva(reserva_obj):
    try:
        reserva_obj.save()
        return True, "Reserva realizada exitosamente."
    except Exception as e:
        return False, f"Error al guardar la reserva: {e}"


def listar_reservas_activas():
    try:
        return list(Reserva.select().where(Reserva.estado == "Reservada"))
    except Exception as e:
        print(f"Error al listar reservas: {e}")
        return []


def buscar_reserva_por_id(id_reserva):
    return Reserva.get_or_none(Reserva.id_reserva == id_reserva)


def cancelar_reserva(id_reserva):
    try:
        reserva = buscar_reserva_por_id(id_reserva)
        if reserva:
            reserva.estado = "Cancelada" 
            reserva.save()
            return True, "Reserva cancelada exitosamente."
        return False, "Reserva no encontrada."
    except Exception as e:
        return False, f"Error al cancelar la reserva: {e}"