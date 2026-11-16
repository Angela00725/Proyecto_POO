# Sistema de Gestión y Reservas de Restaurantes (POO)

Un sistema de consola en Python diseñado bajo los principios de la Programación Orientada a Objetos (POO) y la Arquitectura en Capas, utilizando el ORM Peewee para la persistencia de datos en una base de datos MySQL.

## Características Principales

- Gestión CRUD de restaurantes y clientes.
- Gestión CRUD de mesas asociadas a restaurantes.
- Gestión de reservas: creación, modificación, cancelación y validación de capacidad.
- Estado de reserva: `1 = Reservada`, `2 = Cancelada`, `3 = Completada`.
- Gestión CRUD de usuarios y horarios de atención.
- Validación de RUT, correo y contraseña; las contraseñas de usuario se almacenan con bcrypt.
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
  - `python-decouple`: Para leer la configuración desde variables de entorno (`.env`).
  - `bcrypt`: Para generar hashes seguros de contraseñas.

## Ejecución

1. Configura la conexión a MySQL en el archivo `.env`.
2. Ejecuta el script `datos/sql/01_crear_tablas.sql` en la base de datos.
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Inicia el sistema con `python app.py`.
