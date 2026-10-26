# Sistema de Gestión y Reservas de Restaurantes (POO)

Un sistema de consola en Python diseñado bajo los principios de la Programación Orientada a Objetos (POO) y la Arquitectura en Capas, utilizando el ORM Peewee para la persistencia de datos en una base de datos MySQL.

## Características Principales

- Gestión de Restaurantes: Registro, edición y listado de sucursales activas.
- Gestión de Clientes: Registro de clientes con RUT y control de datos de contacto.
- Gestión de Mesas: Registro de mesas asociadas a restaurantes con control de capacidad física.
- Gestión de Reservas: 
  - Validaciones de reglas de negocio en la capa correspondiente (ej. verificación de capacidad de mesa antes de confirmar).
  - Cancelación y borrado lógico de reservas.
- Interfaz Visual en Consola: Despliegue de tablas formateadas mediante `PrettyTable`.

## Arquitectura del Sistema

El proyecto implementa una arquitectura multicapa con separación limpia de responsabilidades:

1. Capa de Presentación (`presentacion/`): Módulos interactivos en consola (`PrettyTable` y menús).
2. Capa de Negocio (`negocio/`): Contiene la lógica, reglas de validación y flujos de trabajo.
3. Capa de Datos (`datos/`):
   - Modelos (`datos/modelos/`): Clases ORM mapeadas a las tablas de MySQL mediante Peewee.
   - Repositorios (`datos/repositorios/`): Encargados de las operaciones CRUD directas hacia la base de datos.
4. Módulos Auxiliares (`auxiliares/`): Helpers de formato, mensajes globales y utilidades.

## Tecnologías y Librerías

- Lenguaje: Python 3.12
- Base de Datos: MySQL
- ORM: Peewee
- Conector DB: PyMySQL
- Librerías Adicionales:
  - `prettytable`: Para el formato de tablas en consola.
  - `python-decouple`: Para el manejo seguro de variables de entorno (`.env`).