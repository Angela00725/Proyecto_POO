from peewee import IntegrityError, OperationalError, fn

from datos.modelos.cliente import Cliente


def guardar_cliente(cliente_obj):
    try:
        cliente_obj.save()
        return True, "Cliente registrado exitosamente."
    except IntegrityError:
        return False, "Error: El RUT ingresado ya existe."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def listar_clientes_activos():
    return list(Cliente.select().where(Cliente.habilitado == True))


def buscar_cliente_por_rut(rut):
    rut_normalizado = rut.replace(".", "").replace("-", "").strip().upper()
    return Cliente.get_or_none(
        (
            fn.UPPER(fn.REPLACE(fn.REPLACE(Cliente.rut, ".", ""), "-", ""))
            == rut_normalizado
        )
        & (Cliente.habilitado == True)
    )


def buscar_cliente_por_id(id_cliente):
    return Cliente.get_or_none(
        (Cliente.id_cliente == id_cliente) & (Cliente.habilitado == True)
    )


def actualizar_cliente(cliente_obj):
    try:
        cliente_obj.save()
        return True, "Cliente actualizado correctamente."
    except IntegrityError:
        return False, "Error: El RUT ingresado ya existe."
    except OperationalError as error:
        return False, f"Error de conexión con MySQL: {error}"


def eliminar_cliente_logico(rut):
    cliente = buscar_cliente_por_rut(rut)
    if not cliente:
        return False, "Cliente no encontrado."

    cliente.habilitado = False
    return actualizar_cliente(cliente)
