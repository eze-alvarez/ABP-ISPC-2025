# ------   FUNCIÓN LISTAR DESTINOS  --------
def listar_destinos(cursor):
    cursor.execute("SELECT id_destino, ciudad, pais, costo_base, estado FROM destinos")
    destinos = cursor.fetchall()

    print("\n--- DESTINOS REGISTRADOS ---")
    for d in destinos:
        estado = "Activo" if d[4] else "Inactivo"
        print(f"ID: {d[0]} | Ciudad: {d[1]} | País: {d[2]} | Costo: ${d[3]:.2f} | Estado: {estado}")
        
# ------   FUNCIÓN AGREGAR DESTINO  --------
def agregar_destino(cursor, conexion):
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    costo_base = float(input("Costo base ($): "))
    estado = input("¿Está activo? (s/n): ").strip().lower() == 's'

    cursor.execute(
        "INSERT INTO destinos (ciudad, pais, costo_base, estado) VALUES (%s, %s, %s, %s)",
        (ciudad, pais, costo_base, estado)
    )
    conexion.commit()
    print("✅ Destino agregado con éxito.")

# ------   FUNCIÓN MODIFICAR DESTINO  --------
def modificar_destino(cursor, conexion):
    id_destino = input("ID del destino a modificar: ")
    nueva_ciudad = input("Nueva ciudad: ")
    nuevo_pais = input("Nuevo país: ")
    nuevo_costo = float(input("Nuevo costo base ($): "))
    nuevo_estado = input("¿Está activo? (s/n): ").strip().lower() == 's'

    cursor.execute(
        """
        UPDATE destinos 
        SET ciudad = %s, pais = %s, costo_base = %s, estado = %s 
        WHERE id_destino = %s
        """,
        (nueva_ciudad, nuevo_pais, nuevo_costo, nuevo_estado, id_destino)
    )
    conexion.commit()
    print("✏️ Destino modificado correctamente.")

# ------   FUNCIÓN ELIMINAR DESTINO  --------
def eliminar_destino(cursor, conexion):
    id_destino = input("ID del destino a eliminar: ")
    cursor.execute("DELETE FROM destinos WHERE id_destino = %s", (id_destino,))
    conexion.commit()
    print("🗑️ Destino eliminado.")


