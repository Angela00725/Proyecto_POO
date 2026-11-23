from peewee import (
    AutoField,
    BooleanField,
    CharField,
    ForeignKeyField,
    IntegerField,
)

from datos.conexion import ModelBase
from datos.modelos.restaurante import Restaurante

class Mesa(ModelBase):
    id_mesa = AutoField(primary_key=True)
    id_restaurante = ForeignKeyField(
        Restaurante,
        backref="mesas",
        column_name="fk_restaurante",
    )
    numero_mesa = IntegerField()
    capacidad_personas = IntegerField(column_name="capacidad")
    ubicacion = CharField(max_length=100, null=True)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = "mesas"