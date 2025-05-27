"""
SkyRoute - Sistema de Gestión de Pasajes Aéreos
------------------------------------------------
Este sistema es un prototipo simple en consola que simula la gestión de pasajes
para la empresa ficticia SkyRoute S.R.L. Permitirá registrar clientes, destinos y
ventas, así como usar el botón de arrepentimiento para anular compras.

Cómo ejecutar:
1. Asegurarse de tener Python instalado.
2. Abrir la terminal y posicionarse en la carpeta del archivo.
3. Ejecutar con el comando: python main.py

Integrantes del Grupo:
- Alvarez Peredo Gonzalo Ezequiel
- Rubatto Birri Martina Aluminé
- Ibarra Leandro Martín
"""


print("\n -----   Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes    -----")

opcion = ""

# Bucle principal del programa

while opcion != "8":

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del Sistema")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")
    
    # ------   Gestión de clientes  --------
    if opcion == "1":
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")

        subop = input("Seleccione una opción: ")
        if subop == "1":
            print("Mostrando clientes registrados...")

        elif subop == "2":
            razon_social = input("Ingrese razón social: ")
            cuit = input("Ingrese CUIT: ")
            correo = input("Ingrese correo de contacto: ")
            print("Cliente agregado con los siguientes datos:")
            print(f"Razón social: {razon_social}, CUIT: {cuit}, Correo: {correo}")

        elif subop == "3":
            print("Modificar un cliente...")

        elif subop == "4":
            print("Eliminar un cliente...")

        elif subop == "5":
            print("Volviendo al Menú Principal...")

        else:
            print("Opción inválida")

    # ----   Gestión de destinos  --------
    elif opcion == "2":
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")

        subop = input("Seleccione una opción: ")
        print(f"Elegiste la opción {subop} del submenú de destinos...")


    # ------   Gestión de ventas  --------
    elif opcion == "3":
        print("\n-- GESTIONAR VENTAS --")
        print("1. Registrar Venta")
        print("2. Volver al Menú Principal")
        
        subop = input("Seleccione una opción: ")

        if subop == "1":
            print("Registrando una nueva venta...")

        elif subop == "2":
            print("Volviendo al Menú Principal...")

        else:
            print("Opción inválida")



    # ------   Consultar ventas  --------
    elif opcion == "4":
        print("\n-- CONSULTAR VENTAS --")
        print("1. Ver todas")
        print("2. Filtrar por cliente")
        print("3. Ventas de la última semana")
        print("4. Ventas anuladas")
        print("5. Volver al Menú Principal")

        subop = input("Seleccione una opción: ")

        if subop == "1":
            print("Se mostraron todas las ventas registradas.")
            print("Volviendo al Menú Principal...")

        elif subop == "2":
            cliente = input("Ingrese el nombre o CUIT del cliente: ")
            print(f"Se mostraron las ventas filtradas para el cliente: {cliente}")
            print("Volviendo al Menú Principal...")

        elif subop == "3":
            print("Se mostraron las ventas de la última semana...")
            print("Volviendo al Menú Principal...")

        elif subop == "4":
            print("Se mostraron las ventas anuladas mediante el botón de arrepentimiento.")
            print("Volviendo al Menú Principal...")

        elif subop == "5":
            print("Volviendo al Menú Principal...")

        else:
            print("Opción inválida. Regresando al menú principal.")


    # ------   BOTÓN DE ARREPENTIMIENTO  --------
    elif opcion == "5":
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        print("Ingrese el ID de la venta a anular:")
        venta_id = input("ID: ")
        print(f"Venta {venta_id} anulada exitosamente (derecho de arrepentimiento)")


     # ------   REPORTE GENERAL  --------
    elif opcion == "6":
        print("\n-- REPORTE GENERAL --")
        print("Generando informe de ventas, clientes y destinos...")


    # ------    ACERCA DEL SISTEMA   --------
    elif opcion == "7":
        print("\n-- ACERCA DEL SISTEMA --")
        print("SkyRoute - Sistema de Gestión de Pasajes desarrollado por estudiantes.")
        print("Versión: Prototipo - Evidencia 2")


    # ------    Salir del sistema   --------
    elif opcion == "8":
        print("Saliendo del sistema...")


    # ------    Opción inválida   --------
    else:
        print("Opción inválida. Intente nuevamente.")
