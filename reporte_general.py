# ------   FUNCIÓN REPORTE GENERAL  --------
def mostrar_reporte_general(cursor):
    print("\n--- REPORTE GENERAL ---\n")

    # Total de clientes
    cursor.execute("SELECT COUNT(*) FROM clientes")
    total_clientes = cursor.fetchone()[0]
    print(f"Total de clientes registrados: {total_clientes}")

    # Total de destinos
    cursor.execute("SELECT COUNT(*) FROM destinos")
    total_destinos = cursor.fetchone()[0]
    print(f"Total de destinos registrados: {total_destinos}")

    # Total de ventas por estado
    cursor.execute("""
        SELECT estado, COUNT(*) 
        FROM ventas 
        GROUP BY estado
    """)
    ventas_por_estado = cursor.fetchall()
    print("\nVentas por estado:")
    for estado, cantidad in ventas_por_estado:
        print(f" - {estado.capitalize()}: {cantidad}")

    # Ingresos totales por ventas confirmadas
    cursor.execute("""
        SELECT SUM(costo_final) 
        FROM ventas 
        WHERE estado = 'confirmada'
    """)
    ingresos_totales = cursor.fetchone()[0]
    ingresos_totales = ingresos_totales if ingresos_totales else 0.00
    print(f"\nIngresos totales por ventas confirmadas: ${ingresos_totales:,.2f}")

    # Top 5 destinos más vendidos
    cursor.execute("""
        SELECT d.ciudad, d.pais, COUNT(*) AS cantidad_ventas
        FROM ventas v
        JOIN destinos d ON v.id_destino = d.id_destino
        GROUP BY v.id_destino
        ORDER BY cantidad_ventas DESC
        LIMIT 5
    """)
    top_destinos = cursor.fetchall()
    print("\nTop 5 destinos más vendidos:")
    for ciudad, pais, cantidad in top_destinos:
        print(f" - {ciudad}, {pais}: {cantidad} ventas")
