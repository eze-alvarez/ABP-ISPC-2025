-- =======================================
-- SkyRoute S.R.L. - Estructura de Base de Datos
-- Archivo: estructura.sql
-- =======================================

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

-- =======================================
-- Tabla de Clientes
-- =======================================
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    cuit VARCHAR(13) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fecha_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- =======================================
-- Tabla de Destinos
-- =======================================
CREATE TABLE destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(100) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    costo_base DECIMAL(12,2) NOT NULL,
    estado BOOLEAN NOT NULL
);

-- =======================================
-- Tabla de Ventas
-- =======================================
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_destino INT NOT NULL,
    fecha_venta DATETIME NOT NULL,
    costo_final DECIMAL(12,2) NOT NULL,
    estado ENUM('confirmada', 'cancelada', 'pendiente') NOT NULL,
    forma_pago VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);

-- =======================================
-- Tabla de Botón de Arrepentimiento
-- =======================================
CREATE TABLE boton_arrepentimiento (
    id_arrepentimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    fecha_solicitud DATETIME NOT NULL,
    fecha_procesamiento DATETIME,
    estado ENUM('solicitado', 'procesado', 'rechazado') NOT NULL,
    motivo TEXT,
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta)
);
