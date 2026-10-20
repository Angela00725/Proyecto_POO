from peewee import AutoField, CharField, ForeignKeyField, IntegerField, Model

from datos.conexion import conectar_db
from datos.modelos.restaurante import Restaurante

db = conectar_db()


class BaseModel(Model):
    class Meta:
        database = db


class Mesa(BaseModel):
    id_mesa = AutoField(primary_key=True)
    id_restaurante = ForeignKeyField(
        Restaurante,
        backref="mesas",
        column_name="fk_restaurante",
    )
    numero_mesa = IntegerField()
    capacidad_personas = IntegerField(column_name="capacidad")
    ubicacion = CharField(max_length=100, null=True)

    class Meta:
        table_name = "mesas"