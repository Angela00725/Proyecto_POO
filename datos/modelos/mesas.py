from peewee import AutoField, BooleanField, ForeignKeyField, IntegerField, Model
from datos.conexion import db
from datos.modelos.restaurante import Restaurante


class Mesa(Model):
    id_mesa = AutoField(primary_key=True)
    id_restaurante = ForeignKeyField(
        Restaurante, backref="mesas", column_name="id_restaurante"
    )
    numero_mesa = IntegerField()
    capacidad_personas = IntegerField()
    habilitada = BooleanField(default=True)

    class Meta:
        database = db
        table_name = "mesa"