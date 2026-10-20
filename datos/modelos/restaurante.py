from peewee import AutoField, BooleanField, CharField, Model
from datos.conexion import db


class Restaurante(Model):
    id_restaurante = AutoField(primary_key=True)
    nombre = CharField(max_length=100)
    direccion = CharField(max_length=150)
    telefono = CharField(max_length=20, null=True)
    habilitado = BooleanField(default=True)

    class Meta:
        database = db
        table_name = "restaurante"