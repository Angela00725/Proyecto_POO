CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT,
    rut VARCHAR(12) UNIQUE NOT NULL,
    nombre_apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(15),
    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente)
);
 
CREATE TABLE restaurantes (
    id_restaurante INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    telefono VARCHAR(12),
    direccion VARCHAR(100),
    CONSTRAINT pk_restaurantes PRIMARY KEY (id_restaurante)
) COMMENT 'Informacion de restaurantes';
 

CREATE TABLE horarioatencion (
    id_horario INT AUTO_INCREMENT,
    dia_semana VARCHAR(20) NOT NULL,
    hora_apertura TIME NOT NULL,
    hora_cierre TIME NOT NULL,
    id_restaurante INT NOT NULL,
    CONSTRAINT pk_horarioatencion PRIMARY KEY (id_horario),
    CONSTRAINT fk_horario_restaurante FOREIGN KEY (id_restaurante)
        REFERENCES restaurantes(id_restaurante)
);
 

CREATE TABLE mesas (
    id_mesa INT AUTO_INCREMENT,
    numero_mesa INT NOT NULL,
    capacidad INT NOT NULL,
    ubicacion VARCHAR(100),
    id_restaurante INT NOT NULL,
    CONSTRAINT pk_mesas PRIMARY KEY (id_mesa),
    CONSTRAINT fk_mesa_restaurante FOREIGN KEY (id_restaurante)
        REFERENCES restaurantes(id_restaurante),
    CONSTRAINT uq_mesa_por_restaurante UNIQUE (id_restaurante, numero_mesa)
) COMMENT 'Informacion de mesas disponibles';
 

CREATE TABLE reservas (
    id_reserva INT AUTO_INCREMENT,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cantidad_personas INT NOT NULL,
    estado INT NOT NULL DEFAULT 1, 
    id_cliente INT NOT NULL,
    id_restaurante INT NOT NULL,
    id_mesa INT NOT NULL,
 
    CONSTRAINT pk_reservas PRIMARY KEY (id_reserva),
    CONSTRAINT fk_reserva_cliente FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente),
    CONSTRAINT fk_reserva_restaurante FOREIGN KEY (id_restaurante)
        REFERENCES restaurantes(id_restaurante),
    CONSTRAINT fk_reserva_mesa FOREIGN KEY (id_mesa)
        REFERENCES mesas(id_mesa)
) COMMENT 'Informacion de reservas';
 