-- =======================================
-- SkyRoute S.R.L. - Datos y Consultas SQL
-- Archivo: datos_y_consultas.sql
-- =======================================

-- ====================
-- Inserción de datos
-- ====================

-- Insertar clientes
INSERT INTO clientes (razon_social, cuit, email, fecha_alta) VALUES
('Empresa Uno S.A.', '30-12345678-9', 'contacto@empresauno.com', '2024-05-01 09:00:00'),
('Servicios del Norte SRL', '33-98765432-1', 'info@serviciosdelnorte.com', '2024-06-15 14:30:00'),
('Juan Pérez', '27-56789012-3', 'juan.perez@gmail.com', '2024-04-20 11:15:00');

-- Insertar destinos
INSERT INTO destinos (ciudad, pais, costo_base, estado) VALUES
('Santiago', 'Chile', 250.00, TRUE),
('Río de Janeiro', 'Brasil', 300.00, TRUE),
('Buenos Aires', 'Argentina', 150.00, FALSE);

-- Insertar ventas
INSERT INTO ventas (id_cliente, id_destino, fecha_venta, costo_final, estado, forma_pago) VALUES
(1, 1, '2024-06-01 10:00:00', 270.00, 'confirmada', 'tarjeta de crédito'),
(2, 2, '2024-06-02 11:30:00', 320.00, 'confirmada', 'transferencia'),
(3, 3, '2024-06-03 15:45:00', 180.00, 'cancelada', 'efectivo');

-- Insertar arrepentimientos
INSERT INTO boton_arrepentimiento (id_venta, fecha_solicitud, fecha_procesamiento, estado, motivo) VALUES
(3, '2024-06-04 09:00:00', '2024-06-04 10:30:00', 'procesado', 'Error en la compra'),
(2, '2024-06-05 08:15:00', NULL, 'solicitado', 'Cambio de fecha'),
(1, '2024-06-06 12:00:00', NULL, 'solicitado', 'Motivo no especificado');


-- ====================
-- Consultas de ejemplo
-- ====================

-- 1. Listar todos los clientes
SELECT * FROM clientes;

-- 2. Mostrar las ventas realizadas el 2 de junio de 2024
SELECT * FROM ventas WHERE DATE(fecha_venta) = '2024-06-02';

-- 3. Obtener la última venta de cada cliente y su fecha
SELECT v1.*
FROM ventas v1
INNER JOIN (
  SELECT id_cliente, MAX(fecha_venta) AS max_fecha
  FROM ventas
  GROUP BY id_cliente
) v2 ON v1.id_cliente = v2.id_cliente AND v1.fecha_venta = v2.max_fecha;

-- 4. Listar todos los destinos que empiezan con "S"
SELECT * FROM destinos WHERE ciudad LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por país
SELECT d.pais, COUNT(*) AS cantidad_ventas
FROM ventas v
JOIN destinos d ON v.id_destino = d.id_destino
GROUP BY d.pais;
