from peewee import IntegrityError, OperationalError

from datos.modelos.restaurante import Restaurante


def guardar_restaurante(restaurante_obj):
    try:
        restaurante_obj.save()
        return True, "Restaurante registrado exitosamente."
    except IntegrityError:
        return False, "No fue posible registrar el restaurante por sus datos."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def listar_restaurantes_activos():
    return list(
        Restaurante.select().where(Restaurante.habilitado == True)
    )


def buscar_restaurante_por_id(id_restaurante):
    return Restaurante.get_or_none(
        (Restaurante.id_restaurante == id_restaurante)
        & (Restaurante.habilitado == True)
    )


def actualizar_restaurante(restaurante_obj):
    try:
        restaurante_obj.save()
        return True, "Restaurante actualizado correctamente."
    except IntegrityError:
        return False, "No fue posible actualizar el restaurante por sus datos."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def eliminar_restaurante_logico(id_restaurante):
    restaurante = buscar_restaurante_por_id(id_restaurante)
    if not restaurante:
        return False, "Restaurante no encontrado."

    restaurante.habilitado = False
    return actualizar_restaurante(restaurante)
