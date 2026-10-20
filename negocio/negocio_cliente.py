from datos.modelos.cliente import Cliente
from datos.repositorios.cliente_repositorio import (
    actualizar_cliente,
    buscar_cliente_por_rut,
    guardar_cliente,
    listar_clientes_activos,
)


def crear_cliente(rut, nombre_apellido, correo, telefono):
    if not rut.strip() or not nombre_apellido.strip():
        return False, "El RUT y el Nombre son obligatorios."

    nuevo_cliente = Cliente(
        rut=rut.strip(),
        nombre_apellido=nombre_apellido.strip(),
        correo=correo.strip() if correo.strip() else None,
        telefono=telefono.strip() if telefono.strip() else None,
    )
    return guardar_cliente(nuevo_cliente)


def obtener_clientes():
    return listar_clientes_activos()


def modificar_cliente(rut, nuevo_nombre, nuevo_correo, nuevo_telefono):
    cliente = buscar_cliente_por_rut(rut)
    if not cliente:
        return False, f"No se encontró cliente con el RUT '{rut}'."

    if nuevo_nombre.strip():
        cliente.nombre_apellido = nuevo_nombre.strip()
    if nuevo_correo.strip():
        cliente.correo = nuevo_correo.strip()
    if nuevo_telefono.strip():
        cliente.telefono = nuevo_telefono.strip()

    return actualizar_cliente(cliente)