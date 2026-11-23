from peewee import Model, MySQLDatabase
from decouple import config


def conectar_db():
    base_datos = MySQLDatabase(config('db'), 
                            **{
                                'charset': 'utf8mb4', 
                                'host': config('host'), 
                                'port': config('port', cast=int), 
                                'user': config('user'), 
                                'password': config('password')})
    return base_datos

db = conectar_db()


class ModelBase(Model):
    class Meta:
        database = db