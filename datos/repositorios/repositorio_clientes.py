from peewee import IntegrityError, OperationalError
from datos.modelos.cliente import Cliente


def guardar_cliente(cliente_obj):
    try:
        cliente_obj.save()
        return True, "Cliente registrado exitosamente."
    except IntegrityError:
        return False, "Error: El RUT ingresado ya existe en la base de datos."
    except OperationalError as e:
        return False, f"Error de conexión con MySQL: {e}"


def listar_clientes_activos():
    try:
        return list(Cliente.select())
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
        return []


def buscar_cliente_por_rut(rut):
    # Busca directamente por la columna rut
    return Cliente.get_or_none(Cliente.rut == rut.strip())


def actualizar_cliente(cliente_obj):
    try:
        cliente_obj.save()
        return True, "Operación realizada correctamente."
    except Exception as e:
        return False, f"Error al actualizar: {e}"