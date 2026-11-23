from peewee import (
    AutoField,
    BooleanField,
    CharField,
    ForeignKeyField,
    TimeField,
)

from datos.conexion import ModelBase
from datos.modelos.restaurante import Restaurante

class Horarioatencion(ModelBase):
    id_horario = AutoField(primary_key=True)
    dia_semana = CharField(max_length=20)
    hora_apertura = TimeField()
    hora_cierre = TimeField()
    id_restaurante = ForeignKeyField(
        Restaurante,
        backref="horarios",
        column_name="fk_restaurante",
    )
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = "horarioatencion"