from datetime import date, time

from datos.modelos.reserva import ESTADO_RESERVADA, Reserva
from datos.repositorios.repositorio_clientes import buscar_cliente_por_rut
from datos.repositorios.repositorio_mesa import buscar_mesa_por_id
from datos.repositorios.repositorio_reserva import (
    actualizar_reserva,
    buscar_reserva_por_id,
    cancelar_reserva as deshabilitar_reserva,
    guardar_reserva,
    listar_reservas_activas,
    marcar_reserva_completada as completar_reserva_repo,
)


def _convertir_fecha_hora(fecha, hora):
    try:
        fecha_convertida = (
            fecha if isinstance(fecha, date) else date.fromisoformat(fecha)
        )
        hora_convertida = (
            hora if isinstance(hora, time) else time.fromisoformat(hora)
        )
        return fecha_convertida, hora_convertida
    except (TypeError, ValueError):
        return None, None


def crear_reserva(rut_cliente, id_mesa, fecha, hora, cantidad_personas):
    cliente = buscar_cliente_por_rut(rut_cliente)
    if not cliente:
        return False, "No se encontró un cliente activo con ese RUT."

    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        return False, "No se encontró una mesa activa."
    if cantidad_personas <= 0:
        return False, "La cantidad de personas debe ser positiva."
    if cantidad_personas > mesa.capacidad_personas:
        return False, (
            f"La cantidad de personas ({cantidad_personas}) excede la capacidad "
            f"de la mesa ({mesa.capacidad_personas})."
        )

    fecha_convertida, hora_convertida = _convertir_fecha_hora(fecha, hora)
    if fecha_convertida is None:
        return False, "La fecha u hora no tienen un formato válido."

    reserva = Reserva(
        id_cliente=cliente,
        id_restaurante=mesa.id_restaurante,
        id_mesa=mesa,
        fecha_reserva=fecha_convertida,
        hora_reserva=hora_convertida,
        cantidad_personas=cantidad_personas,
        estado=ESTADO_RESERVADA,
        habilitado=True,
    )
    return guardar_reserva(reserva)


def obtener_reservas():
    return listar_reservas_activas()


def modificar_reserva(id_reserva, fecha, hora, cantidad_personas):
    reserva = buscar_reserva_por_id(id_reserva)
    if not reserva or reserva.estado != ESTADO_RESERVADA:
        return False, "Reserva activa no encontrada."
    if cantidad_personas <= 0:
        return False, "La cantidad de personas debe ser positiva."
    if cantidad_personas > reserva.id_mesa.capacidad_personas:
        return False, "La cantidad de personas supera la capacidad de la mesa."

    fecha_convertida, hora_convertida = _convertir_fecha_hora(fecha, hora)
    if fecha_convertida is None:
        return False, "La fecha u hora no tienen un formato válido."

    reserva.fecha_reserva = fecha_convertida
    reserva.hora_reserva = hora_convertida
    reserva.cantidad_personas = cantidad_personas
    return actualizar_reserva(reserva)


def cancelar_reserva(id_reserva):
    return deshabilitar_reserva(id_reserva)


def marcar_reserva_completada(id_reserva):
    return completar_reserva_repo(id_reserva)
