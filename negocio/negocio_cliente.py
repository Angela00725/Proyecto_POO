from datos.modelos.cliente import Cliente
from datos.repositorios.repositorio_clientes import (
    actualizar_cliente,
    buscar_cliente_por_rut,
    eliminar_cliente_logico as deshabilitar_cliente,
    guardar_cliente,
    listar_clientes_activos,
)
from auxiliares.validar_rut import validar_rut
from auxiliares.validaciones import validar_correo


def crear_cliente(rut, nombre_apellido, correo, telefono):
    rut_valido, rut_resultado = validar_rut(rut)
    if not rut_valido:
        return False, rut_resultado
    if not nombre_apellido.strip():
        return False, "El nombre del cliente es obligatorio."
    if correo.strip():
        correo_valido, correo_resultado = validar_correo(correo)
        if not correo_valido:
            return False, correo_resultado
        correo = correo_resultado

    nuevo_cliente = Cliente(
        rut=rut_resultado,
        nombre_apellido=nombre_apellido.strip(),
        correo=correo.strip() or None,
        telefono=telefono.strip() or None,
        habilitado=True,
    )
    return guardar_cliente(nuevo_cliente)


def obtener_clientes():
    return listar_clientes_activos()


def modificar_cliente(rut, nuevo_nombre, nuevo_correo, nuevo_telefono):
    rut_valido, rut_resultado = validar_rut(rut)
    if not rut_valido:
        return False, rut_resultado
    cliente = buscar_cliente_por_rut(rut_resultado)
    if not cliente:
        return False, f"No se encontró cliente con el RUT '{rut_resultado}'."

    if nuevo_nombre.strip():
        cliente.nombre_apellido = nuevo_nombre.strip()
    if nuevo_correo.strip():
        correo_valido, correo_resultado = validar_correo(nuevo_correo)
        if not correo_valido:
            return False, correo_resultado
        cliente.correo = correo_resultado
    if nuevo_telefono.strip():
        cliente.telefono = nuevo_telefono.strip()

    return actualizar_cliente(cliente)


def eliminar_cliente_logico(rut):
    rut_valido, rut_resultado = validar_rut(rut)
    if not rut_valido:
        return False, rut_resultado
    return deshabilitar_cliente(rut_resultado)
