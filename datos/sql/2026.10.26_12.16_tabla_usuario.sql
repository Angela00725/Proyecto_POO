CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    correo VARCHAR(191) NOT NULL UNIQUE,
    fecha_nacimiento DATE NULL,
    genero INT NOT NULL,
    fecha_incorporacion DATE NOT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    password VARCHAR(60) NOT NULL
);