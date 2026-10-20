from peewee import Model, AutoField, CharField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database
 
class Cliente(BaseModel):
    correo = CharField(max_length=100, null = True)
    id_cliente = AutoField()
    nombre_apellido = CharField(max_length = 50)
    rut = CharField(max_length=12, unique=True)
    telefono = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'cliente'