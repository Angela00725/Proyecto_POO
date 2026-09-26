create database sistema_reservas_restaurante;
use sistema_reservas_restaurante;

CREATE TABLE cliente (
    id_cliente INTEGER AUTO_INCREMENT NOT NULL,
    rut VARCHAR(10) UNIQUE NOT NULL,
    nombre_apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100),
    CONSTRAINT pk_id_cliente PRIMARY KEY (id_cliente)
)


create table reservas comment 'informacion de reservas'(
    id_reserva auto increment,
    fecha date,
    hora
    cantidad_personas
    estado
    id_restaurante varchar (50),
    id_mesa int
    constraint pk_reservas primary key (id_reserva)
);


CREATE TABLE horarioatencion (
    id_horario INT PRIMARY KEY AUTO_INCREMENT,
    dia_semana VARCHAR (20)NOT NULL ,
    hora_apertura TIME NOT NULL,
    hora_cierre TIME NOT NULL

);

create table mesas comment 'informacion de mesas disponibles'(
    numero_mesa int,
    capacidad int,
    ubicacion varchar (100)
    constraint pk_mesas primary key (numero_mesa)
);

create table restaurantes comment 'informacion de restaurantes'(
    nombre varchar (50),
    telefono varchar (12),
    direccion varchar (100)
    constraint pk_restaurantes primary key (nombre)
);

create table parametros (
    id_parametros int autoincrement primary key,
    tipo_parametro varchar (50) not null,
    descripcion varchar (100) not  null
);