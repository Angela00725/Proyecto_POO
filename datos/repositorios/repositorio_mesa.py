from datos.modelos.mesa import Mesa


def guardar_mesa(mesa_obj):
    try:
        mesa_obj.save()
        return True, "Mesa registrada exitosamente."
    except Exception as e:
        return False, f"Error al guardar la mesa: {e}"


def listar_mesas_activas():
    try:
        return list(Mesa.select().where(Mesa.habilitada == True))
    except Exception as e:
        print(f"Error al listar mesas: {e}")
        return []


def buscar_mesa_por_id(id_mesa):
    return Mesa.get_or_none(
        (Mesa.id_mesa == id_mesa) & (Mesa.habilitada == True)
    )


def actualizar_mesa(mesa_obj):
    try:
        mesa_obj.save()
        return True, "Mesa actualizada correctamente."
    except Exception as e:
        return False, f"Error al actualizar la mesa: {e}"