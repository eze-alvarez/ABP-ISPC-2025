import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if db.is_connected():
            print("Conexión exitosa a la base de datos")
            return db
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
