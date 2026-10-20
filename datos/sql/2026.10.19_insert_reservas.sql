INSERT INTO reservas (fk_cliente, fk_restaurante, fk_mesa, fecha, hora, cantidad_personas, estado, habilitado) VALUES
(2, 1, 3, '2026-10-26', '13:30:00', 4, 'Reservada', TRUE),
(3, 1, 4, '2026-10-26', '20:00:00', 5, 'Reservada', TRUE),
(4, 2, 2, '2026-10-27', '14:00:00', 2, 'Reservada', TRUE),
(5, 2, 3, '2026-10-27', '21:00:00', 4, 'Reservada', TRUE),
(6, 3, 1, '2026-10-28', '13:00:00', 3, 'Completada', TRUE),
(7, 3, 2, '2026-10-28', '20:30:00', 8, 'Reservada', TRUE),
(8, 4, 1, '2026-10-29', '15:00:00', 2, 'Reservada', TRUE),
(9, 4, 2, '2026-10-29', '21:30:00', 4, 'Reservada', TRUE),
(10, 5, 1, '2026-10-30', '13:00:00', 2, 'Cancelada', FALSE),
(11, 5, 2, '2026-10-30', '20:00:00', 6, 'Reservada', TRUE);