from datetime import datetime

# ------   FUNCIÓN REGISTRAR VENTA  --------
def registrar_venta(cursor, conexion):
    print("REGISTRO DE VENTA")

    id_cliente = input("ID del cliente: ")
    id_destino = input("ID del destino: ")
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    costo_final = float(input("Costo final ($): "))

    estado_input = input("Estado (activa/anulada): ").strip().lower()
    if estado_input == "activa":
        estado = "confirmada"
    elif estado_input == "anulada":
        estado = "cancelada"
    else:
        print("Estado inválido. Se usará 'pendiente' por defecto.")
        estado = "pendiente"

    forma_pago = input("Forma de pago (efectivo, tarjeta, etc.): ")

    cursor.execute("""
        INSERT INTO ventas (id_cliente, id_destino, fecha_venta, costo_final, estado, forma_pago)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (id_cliente, id_destino, fecha_venta, costo_final, estado, forma_pago))

    conexion.commit()
    print("Venta registrada con éxito ✅")
    
# ------   FUNCIÓN VER TODAS LAS VENTAS  --------
def ver_todas_las_ventas(cursor):
    cursor.execute("""
        SELECT 
            v.id_venta,
            c.razon_social,
            d.ciudad,
            v.fecha_venta,
            v.costo_final,
            v.estado,
            v.forma_pago
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        JOIN destinos d ON v.id_destino = d.id_destino
        ORDER BY v.fecha_venta DESC
    """)
    ventas = cursor.fetchall()

    print("TODAS LAS VENTAS REGISTRADAS:")
    for v in ventas:
        print(f"ID: {v[0]} | Cliente: {v[1]} | Destino: {v[2]} | Fecha: {v[3].strftime('%d/%m/%Y')} | Monto: ${v[4]:.2f} | Estado: {v[5]} | Pago: {v[6]}")

