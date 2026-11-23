from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    TimeField,
)

from datos.conexion import ModelBase
from datos.modelos.cliente import Cliente
from datos.modelos.mesas import Mesa
from datos.modelos.restaurante import Restaurante

ESTADO_RESERVADA = 1
ESTADO_CANCELADA = 2
ESTADO_COMPLETADA = 3


class Reserva(ModelBase):
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
    estado = IntegerField(default=ESTADO_RESERVADA)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = "reservas"