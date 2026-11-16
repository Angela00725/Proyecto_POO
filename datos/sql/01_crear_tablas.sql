CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre_apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(15),
    habilitado BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE restaurantes (
    id_restaurante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    telefono VARCHAR(20),
    habilitado BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    correo VARCHAR(191) NOT NULL UNIQUE,
    fecha_nacimiento DATE,
    genero INT NOT NULL,
    fecha_incorporacion DATE NOT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    password VARCHAR(60) NOT NULL
);

CREATE TABLE horarioatencion (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    dia_semana VARCHAR(20) NOT NULL,
    hora_apertura TIME NOT NULL,
    hora_cierre TIME NOT NULL,
    fk_restaurante INT NOT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_horario_restaurante FOREIGN KEY (fk_restaurante)
        REFERENCES restaurantes(id_restaurante)
);

CREATE TABLE mesas (
    id_mesa INT AUTO_INCREMENT PRIMARY KEY,
    numero_mesa INT NOT NULL,
    capacidad INT NOT NULL,
    ubicacion VARCHAR(100),
    fk_restaurante INT NOT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_mesa_restaurante FOREIGN KEY (fk_restaurante)
        REFERENCES restaurantes(id_restaurante),
    CONSTRAINT uq_mesa_por_restaurante UNIQUE (fk_restaurante, numero_mesa)
);

CREATE TABLE reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cantidad_personas INT NOT NULL,
    estado INT NOT NULL DEFAULT 1,
    fk_cliente INT NOT NULL,
    fk_restaurante INT NOT NULL,
    fk_mesa INT NOT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_reserva_cliente FOREIGN KEY (fk_cliente)
        REFERENCES cliente(id_cliente),
    CONSTRAINT fk_reserva_restaurante FOREIGN KEY (fk_restaurante)
        REFERENCES restaurantes(id_restaurante),
    CONSTRAINT fk_reserva_mesa FOREIGN KEY (fk_mesa)
        REFERENCES mesas(id_mesa)
);
