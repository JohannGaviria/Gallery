# Importa las librerías y módulos necesarios.
from src.utils.Logger import Logger
from mysql.connector import Error
import mysql.connector
import traceback

# Función para establecer una conexión a la base de datos MySQL.
def connectionDB():
    try:
        # Intenta conectarse a la base de datos utilizando los parámetros de conexión.
        mysdb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gallery",
            auth_plugin='mysql_native_password'
        )
        
        if mysdb.is_connected():
            # Imprime un mensaje de éxito si la conexión se realiza correctamente.
            print("Conexión exitosa a la base de datos.")
            return mysdb
    except Error as ex:
        # Registra errores en el registro de la aplicación en caso de fallo en la conexión.
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return None
