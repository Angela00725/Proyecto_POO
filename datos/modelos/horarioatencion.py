from peewee import (
    AutoField,
    BooleanField,
    CharField,
    ForeignKeyField,
    Model,
    TimeField,
)

from datos.conexion import conectar_db
from datos.modelos.restaurante import Restaurante

db = conectar_db()


class BaseModel(Model):
    class Meta:
        database = db


class Horarioatencion(BaseModel):
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