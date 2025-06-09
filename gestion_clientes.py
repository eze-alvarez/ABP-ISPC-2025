from conexion_base_datos import conectar

# ------   FUNCIÓN VER CLIENTES  --------
def ver_clientes():
    conexion = conectar()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()

    if resultados:
        print("\n--- Clientes Registrados ---")
        for cliente in resultados:
            print(f"ID: {cliente['id_cliente']} - Razón Social: {cliente['razon_social']} - CUIT: {cliente['cuit']} - Email: {cliente['email']}")
    else:
        print("No hay clientes registrados.")

    cursor.close()
    conexion.close()

# ------   FUNCIÓN AGREGAR CLIENTES  --------
def agregar_cliente():
    print("\n-- AGREGAR CLIENTE --")
    razon_social = input("Ingrese razón social: ")
    cuit = input("Ingrese CUIT: ")
    email = input("Ingrese correo electrónico: ")

    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO clientes (razon_social, cuit, email)
                VALUES (%s, %s, %s)
            """
            valores = (razon_social, cuit, email)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("✅ Cliente agregado exitosamente.")
        except Exception as e:
            print(f"❌ Error al agregar cliente: {e}")
        finally:
            cursor.close()
            conexion.close()

# ------   FUNCIÓN MODIFICAR CLIENTES  --------
def modificar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        print("\n-- MODIFICAR CLIENTE --")
        cursor.execute("SELECT id_cliente, razon_social FROM clientes")
        clientes = cursor.fetchall()
        if not clientes:
            print("No hay clientes registrados.")
            return

        print("Clientes registrados:")
        for cliente in clientes:
            print(f"ID: {cliente[0]} - Razón Social: {cliente[1]}")

        id_cliente = int(input("Ingrese el ID del cliente que desea modificar: "))

        # Verificamos si existe
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()
        if cliente is None:
            print("❌ Cliente no encontrado.")
            return

        print("Deje el campo vacío si no desea modificar ese dato.")
        nueva_razon = input("Nueva razón social: ") or cliente[1]
        nuevo_cuit = input("Nuevo CUIT: ") or cliente[2]
        nuevo_email = input("Nuevo email: ") or cliente[3]

        cursor.execute("""
            UPDATE clientes
            SET razon_social = %s, cuit = %s, email = %s
            WHERE id_cliente = %s
        """, (nueva_razon, nuevo_cuit, nuevo_email, id_cliente))

        conexion.commit()
        print("✅ Cliente modificado correctamente.")
    
    except Exception as e:
        print(f"❌ Error al modificar cliente: {e}")
    finally:
        cursor.close()
        conexion.close()

# ------   FUNCIÓN ELIMINAR CLIENTES  --------
def eliminar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        print("\n-- ELIMINAR CLIENTE --")
        cursor.execute("SELECT id_cliente, razon_social FROM clientes")
        clientes = cursor.fetchall()

        if not clientes:
            print("No hay clientes registrados.")
            return

        print("Clientes registrados:")
        for cliente in clientes:
            print(f"ID: {cliente[0]} - Razón Social: {cliente[1]}")

        id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))

        # Confirmamos que existe
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()
        if not cliente:
            print("❌ Cliente no encontrado.")
            return

        confirmacion = input(f"¿Está seguro que desea eliminar al cliente '{cliente[1]}'? (s/n): ").lower()
        if confirmacion != 's':
            print("❌ Operación cancelada.")
            return

        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
        conexion.commit()
        print("✅ Cliente eliminado correctamente.")

    except Exception as e:
        print(f"❌ Error al eliminar cliente: {e}")
    finally:
        cursor.close()
        conexion.close()