from peewee import AutoField, CharField, ForeignKeyField, Model, TimeField

from datos.conexion import conectar_db
from datos.modelos.restaurante import Restaurante

# Conexión a la base de datos
db = conectar_db()


class BaseModel(Model):
    class Meta:
        database = db


class Horarioatencion(BaseModel):
    id_horario = AutoField(primary_key=True)
    dia_semana = CharField(max_length=20)
    hora_apertura = TimeField()
    hora_cierre = TimeField()
    # Clave foránea que conecta con la sucursal de Restaurante
    id_restaurante = ForeignKeyField(
        Restaurante,
        backref="horarios",
        column_name="id_restaurante",
    )

    class Meta:
        table_name = "horarioatencion"