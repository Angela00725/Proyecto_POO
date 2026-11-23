from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    IntegerField,
)

from datos.conexion import ModelBase


class Usuario(ModelBase):
    id_usuario = AutoField(primary_key=True)
    rut = CharField(max_length=12, unique=True)
    nombre = CharField(max_length=25)
    apellido = CharField(max_length=25)
    correo = CharField(max_length=191, unique=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField()
    fecha_incorporacion = DateField()
    habilitado = BooleanField(default=True)
    password = CharField(max_length=60)

    class Meta:
        table_name = "usuarios"