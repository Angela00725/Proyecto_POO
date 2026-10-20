from datos.modelos.reserva import Reserva
from datos.repositorios.repositorio_mesa import buscar_mesa_por_id
from datos.repositorios.repositorio_reserva import (
    buscar_reserva_por_id,
    cancelar_reserva as cancelar_reserva_repo,
    guardar_reserva,
    listar_reservas_activas,
)


def crear_reserva(id_cliente, id_restaurante, id_mesa, fecha, hora, cantidad_personas):
    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        return False, "La mesa seleccionada no existe."

    if cantidad_personas > mesa.capacidad_personas:
        return False, f"La cantidad de personas ({cantidad_personas}) excede la capacidad de la mesa ({mesa.capacidad_personas})."

    reserva = Reserva(
        id_cliente=id_cliente,
        id_restaurante=id_restaurante,
        id_mesa=id_mesa,
        fecha_reserva=fecha,
        hora_reserva=hora,
        cantidad_personas=cantidad_personas,
        estado="Reservada",
    )
    return guardar_reserva(reserva)


def obtener_reservas():
    return listar_reservas_activas()


def cancelar_reserva(id_reserva):
    return cancelar_reserva_repo(id_reserva)