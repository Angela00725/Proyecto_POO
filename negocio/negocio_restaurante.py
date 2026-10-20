from datos.modelos.restaurante import Restaurante
from datos.repositorios.restaurante_repositorio import (
    actualizar_restaurante,
    buscar_restaurante_por_id,
    guardar_restaurante,
    listar_restaurantes_activos,
)


def crear_restaurante(nombre, direccion, telefono):
    if not nombre.strip() or not direccion.strip():
        return False, "El nombre y la dirección son obligatorios."

    nuevo_restaurante = Restaurante(
        nombre=nombre.strip(),
        direccion=direccion.strip(),
        telefono=telefono.strip() if telefono.strip() else None,
        habilitado=True,
    )
    return guardar_restaurante(nuevo_restaurante)


def obtener_restaurantes():
    return listar_restaurantes_activos()


def modificar_restaurante(id_restaurante, nuevo_nombre, nueva_direccion, nuevo_telefono):
    restaurante = buscar_restaurante_por_id(id_restaurante)
    if not restaurante:
        return False, f"No se encontró un restaurante activo con ID {id_restaurante}."

    if nuevo_nombre.strip():
        restaurante.nombre = nuevo_nombre.strip()
    if nueva_direccion.strip():
        restaurante.direccion = nueva_direccion.strip()
    if nuevo_telefono.strip():
        restaurante.telefono = nuevo_telefono.strip()

    return actualizar_restaurante(restaurante)


def eliminar_restaurante_logico(id_restaurante):
    restaurante = buscar_restaurante_por_id(id_restaurante)
    if not restaurante:
        return False, f"No se encontró un restaurante activo con ID {id_restaurante}."

    restaurante.habilitado = False
    return actualizar_restaurante(restaurante)