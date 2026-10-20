from datos.modelos.mesas import Mesa
from datos.repositorios.repositorio_mesa import (
    actualizar_mesa,
    buscar_mesa_por_id,
    guardar_mesa,
    listar_mesas_activas,
)
from datos.repositorios.repositorio_restaurante import buscar_restaurante_por_id


def crear_mesa(id_restaurante, numero_mesa, capacidad):
    restaurante = buscar_restaurante_por_id(id_restaurante)
    if not restaurante:
        return False, f"No existe un restaurante activo con ID {id_restaurante}."

    if numero_mesa <= 0 or capacidad <= 0:
        return False, "El número de mesa y la capacidad deben ser valores positivos."

    nueva_mesa = Mesa(
        id_restaurante=restaurante,
        numero_mesa=numero_mesa,
        capacidad_personas=capacidad,
        habilitada=True,
    )
    return guardar_mesa(nueva_mesa)


def obtener_mesas():
    return listar_mesas_activas()


def eliminar_mesa_logico(id_mesa):
    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        return False, f"No se encontró una mesa activa con ID {id_mesa}."

    mesa.habilitada = False
    return actualizar_mesa(mesa)