INSERT INTO usuarios (
    rut,
    nombre,
    apellido,
    correo,
    fecha_nacimiento,
    genero,
    fecha_incorporacion,
    habilitado,
    password
)
SELECT
    '12345678-5',
    'Usuario',
    'Demo',
    'demo.usuario@example.com',
    NULL,
    3,
    CURDATE(),
    TRUE,
    '$2b$12$N.iymZG19SK7OVOaRFxwUe1WuuduHujaHqPd.SdplJpzNsWc/qd.2'
WHERE NOT EXISTS (
    SELECT 1
    FROM usuarios
    WHERE rut = '12345678-5'
       OR correo = 'demo.usuario@example.com'
);
