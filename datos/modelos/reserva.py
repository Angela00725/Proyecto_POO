from peewee import (
    AutoField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    TimeField,
)

from datos.conexion import conectar_db
from datos.modelos.cliente import Cliente
from datos.modelos.mesas import Mesa
from datos.modelos.restaurante import Restaurante

db = conectar_db()


class BaseModel(Model):
    class Meta:
        database = db


class Reserva(BaseModel):
    id_reserva = AutoField(primary_key=True)
    id_cliente = ForeignKeyField(
        Cliente, backref="reservas", column_name="fk_cliente"
    )
    id_restaurante = ForeignKeyField(
        Restaurante, backref="reservas", column_name="fk_restaurante"
    )
    id_mesa = ForeignKeyField(
        Mesa, backref="reservas", column_name="fk_mesa"
    )
    fecha_reserva = DateField(column_name="fecha")
    hora_reserva = TimeField(column_name="hora")
    cantidad_personas = IntegerField()
    estado = CharField(default="Reservada")

    class Meta:
        table_name = "reservas"