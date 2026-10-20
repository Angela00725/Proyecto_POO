from datos.modelos.reservas import Reserva
from datos.repositorios.repositorio_clientes import buscar_cliente_por_rut
from datos.repositorios.repositorio_mesa import buscar_mesa_por_id
from datos.repositorios.repositorio_reserva import (
    actualizar_reserva,
    buscar_reserva_por_id,
    guardar_reserva,
    listar_reservas_activas,
)


def crear_reserva(rut_cliente, id_mesa, fecha, hora, cantidad_personas):
    cliente = buscar_cliente_por_rut(rut_cliente)
    if not cliente:
        return False, f"No existe un cliente activo con el RUT '{rut_cliente}'."

    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        return False, f"No existe una mesa activa con ID {id_mesa}."

    if cantidad_personas > mesa.capacidad_personas:
        return False, f"La mesa seleccionada solo tiene capacidad para {mesa.capacidad_personas} personas."

    nueva_reserva = Reserva(
        id_cliente=cliente,
        id_restaurante=mesa.id_restaurante,
        id_mesa=mesa,
        fecha_reserva=fecha,
        hora_reserva=hora,
        cantidad_personas=cantidad_personas,
        estado="Reservada",
        habilitado=True,
    )
    return guardar_reserva(nueva_reserva)


def obtener_reservas():
    return listar_reservas_activas()


def cancelar_reserva(id_reserva):
    reserva = buscar_reserva_por_id(id_reserva)
    if not reserva:
        return False, f"No se encontró una reserva activa con ID {id_reserva}."

    reserva.estado = "Cancelada"
    reserva.habilitado = False
    return actualizar_reserva(reserva)