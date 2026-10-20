from peewee import OperationalError
from datos.modelos.restaurante import Restaurante


def guardar_restaurante(restaurante_obj):
    try:
        restaurante_obj.save()
        return True, "Restaurante registrado exitosamente."
    except OperationalError as e:
        return False, f"Error de conexión: {e}"


def listar_restaurantes_activos():
    try:
        return list(Restaurante.select().where(Restaurante.habilitado == True))
    except Exception as e:
        print(f"Error al consultar restaurantes: {e}")
        return []


def buscar_restaurante_por_id(id_restaurante):
    return Restaurante.get_or_none(
        (Restaurante.id_restaurante == id_restaurante)
        & (Restaurante.habilitado == True)
    )


def actualizar_restaurante(restaurante_obj):
    try:
        restaurante_obj.save()
        return True, "Restaurante actualizado correctamente."
    except Exception as e:
        return False, f"Error al actualizar: {e}"