CREATE database mecapp;
USE mecapp;

CREATE TABLE tipos_direcciones {
    id_tipo_direcion INTEGER AUTO_INCREMENT,
    tipo_direccion VARCHAR(25) NOT NULL,
    detalle VARCHAR(50) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tipos_direccion PRIMARY KEY (id_tipo_direcion) 
}

CREATE TABLE comunas{
    id_comuna INTEGER AUTO_INCREMENT,
    codigo_comuna VARCHAR(5) NOT NULL UNIQUE,
    nombre_comuna VARCHAR(30) NOT NULL,

CONSTRAINT pk_comunas PRIMARY KEY (id_comuna, codigo_comuna)
}

CREATE TABLE direcciones {
    id_direccion INTEGER AUTO_INCREMENT,
    comuna INTEGER NOT NULL,
    calle VARCHAR(50)  NOT NULL,
    numero_direccion VARCHAR(5) NULL,
    departamento VARCHAR(5) NULL,
    tipo_direccion INTEGER NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direcion),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (comuna) REFERENCES comunas(id_comuna),
    CONSTRAINT fk_direcciones_tipos_direcciones FOREIGN KEY (tipo_direccione) REFERENCES tipos_direccion(id_tipos_direccion)

}
ALTER TABLE tipos_direccion comment ='tipos de oficina';
ALTER TABLE tipos_direccion comment ='tipos de oficina';
ALTER TABLE tipos_direccion comment ='tipos de oficina';
ALTER TABLE tipos_direccion comment ='tipos de oficina';


Create TABLE talleres (
    id_taller INTEGER AUTO_INCREMENT,
    nombre_taller VARCHAR(50) NOT NULL,
    direccion INTEGER NOT NULL,
    CONSTRAINT pk_talleres PRIMARY KEY (id_taller),
    CONSTRAINT fk_talleres_direcciones FOREIGN KEY (id_direccion)
    comment = 'Informacion de talleres mecánicos.' 
)

CREATE TABLE tipos_mecanicos (
    id_tipo_mecanico INTEGER AUTO_INCREMENT,
    tipo_mecanico VARCHAR (25) NOT NULL,
    detalle VARCHAR(50)
)
