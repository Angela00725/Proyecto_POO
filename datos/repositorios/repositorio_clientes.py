from datos.modelos.cliente import Cliente

def listado_clientes():
    clientes = Cliente.select()
    if clientes:
        return clientes

def guardar_pais(pais:Pais):
    try:
        guardar_pais = pais.save()
        if guardar_pais == 1:
            print(f'Pais guardado con éxito con Id: {pais.id_pais}.')
    except IntegrityError as e:
        print(f"Error de clave unica o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional\n(pérdida de conexión, falta una tabla o base de datos bloqueada): {e}")
    except DataError as e:
        # Handles data values out of range or incorrect formats
        print(f"Valor insertdo NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def modificar_cliente():
    try:
        while 
    except Exception as error:
        print(f'ha ocurrido un error: {error}')