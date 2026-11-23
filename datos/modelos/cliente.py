from peewee import AutoField, BooleanField, CharField

from datos.conexion import ModelBase


class Cliente(ModelBase):
    id_cliente = AutoField()
    rut = CharField(max_length=12, unique=True)
    nombre_apellido = CharField(max_length=50)
    correo = CharField(max_length=100, null=True)
    telefono = CharField(max_length=15, null=True)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = "cliente"