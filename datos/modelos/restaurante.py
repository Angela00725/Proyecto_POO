from peewee import AutoField, BooleanField, CharField, Model

from datos.conexion import conectar_db

db = conectar_db()


class BaseModel(Model):
    class Meta:
        database = db


class Restaurante(BaseModel):
    id_restaurante = AutoField(primary_key=True)
    nombre = CharField(max_length=100)
    direccion = CharField(max_length=150)
    telefono = CharField(max_length=20, null=True)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = "restaurantes"