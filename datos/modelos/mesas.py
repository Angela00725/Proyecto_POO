from peewee import AutoField, BooleanField, ForeignKeyField, IntegerField, Model

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
        column_name="id_restaurante",
    )
    numero_mesa = IntegerField()
    capacidad_personas = IntegerField()
    habilitada = BooleanField(default=True)

    class Meta:
        table_name = "mesa"