from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    TimeField,
)
from datos.conexion import db
from datos.modelos.cliente import Cliente
from datos.modelos.mesa import Mesa


class Reserva(Model):
    id_reserva = AutoField(primary_key=True)
    id_cliente = ForeignKeyField(
        Cliente, backref="reservas", column_name="id_cliente"
    )
    id_mesa = ForeignKeyField(
        Mesa, backref="reservas", column_name="id_mesa"
    )
    fecha_reserva = DateField()
    hora_reserva = TimeField()
    cantidad_personas = IntegerField()
    estado = CharField(default="Reservada")
    habilitado = BooleanField(default=True)

    class Meta:
        database = db
        table_name = "reserva"