from conexion_base_datos import conectar
from datetime import datetime, timedelta

# ------   FUNCIÓN BOTON DE ARREPENTIMIENTO  --------
def ejecutar_boton_arrepentimiento():
    conexion = conectar()
    cursor = conexion.cursor()

    try:

        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        # 1. Buscar ventas confirmadas en los últimos 5 minutos
        cursor.execute("""
            SELECT v.id_venta, c.razon_social, CONCAT(d.ciudad, ', ', d.pais) AS destino, v.fecha_venta, v.costo_final
            FROM ventas v
            JOIN clientes c ON v.id_cliente = c.id_cliente
            JOIN destinos d ON v.id_destino = d.id_destino
            WHERE v.estado = 'confirmada'
            AND v.fecha_venta >= NOW() - INTERVAL 5 MINUTE

        """)
        ventas = cursor.fetchall()

        if not ventas:
            print("❌ No hay ventas confirmadas en los últimos 5 minutos.")
            return

        print("\n🧾 Ventas recientes disponibles para anular:")
        for v in ventas:
            print(f"ID: {v[0]} | Cliente: {v[1]} | Destino: {v[2]} | Fecha: {v[3]} | Total: ${v[4]}")

        id_venta = input("\nIngrese el ID de la venta que desea anular: ")

        # 2. Validar que la venta ingresada esté entre las recientes
        venta_ids_validos = [str(v[0]) for v in ventas]
        if id_venta not in venta_ids_validos:
            print("⚠️ El ID ingresado no corresponde a una venta reciente.")
            return

        # 3. Obtener detalles de la venta seleccionada
        cursor.execute("SELECT fecha_venta, estado FROM ventas WHERE id_venta = %s", (id_venta,))
        resultado = cursor.fetchone()

        if not resultado:
            print("❌ Venta no encontrada.")
            return

        fecha_venta, estado_actual = resultado

        if estado_actual == "cancelada":
            print("⚠️ La venta ya fue cancelada anteriormente.")
            return

        ahora = datetime.now()
        diferencia = ahora - fecha_venta

        if diferencia > timedelta(minutes=5):
            print("⏱️ El plazo de 5 minutos para arrepentimiento ha expirado.")
            return

        # 4. Actualizar estado de la venta
        cursor.execute("UPDATE ventas SET estado = 'cancelada' WHERE id_venta = %s", (id_venta,))

        # 5. Registrar el arrepentimiento
        cursor.execute("""
            INSERT INTO boton_arrepentimiento (id_venta, fecha_solicitud, fecha_procesamiento, estado, motivo)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_venta, ahora, ahora, "procesado", "Arrepentimiento dentro del plazo"))

        conexion.commit()
        print(f"✅ Venta {id_venta} anulada exitosamente por arrepentimiento.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        cursor.close()
        conexion.close()
