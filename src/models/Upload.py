# Importa las librerías y módulos necesarios.
from werkzeug.utils import secure_filename
from src.utils.Logger import Logger
from flask import flash
import os
import random
import string
import traceback

# Clase que maneja la carga y almacenamiento de imágenes.
class UploadHandler:
    def __init__(self, file, upload_folder):
        self.file = file
        self.upload_folder = upload_folder

    # Genera un nombre de archivo aleatorio para la imagen.
    def generate_random_filename(self):
        random_name = ''.join(random.choices(string.digits, k=10))
        return random_name

    # Verifica si el archivo tiene una extensión válida de imagen.
    def is_image(self, filename):
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    # Guarda la imagen en el servidor y maneja posibles errores.
    def save_image(self):
        try:
            if self.file.filename == '':
                flash("El archivo no tiene nombre.", "danger")
                return None

            if not self.is_image(self.file.filename):
                flash("El archivo no es una imagen válida.", "danger")
                return None

            random_filename = self.generate_random_filename()

            # Genera un nombre de archivo seguro utilizando la función secure_filename.
            filename = secure_filename(random_filename + os.path.splitext(self.file.filename)[1])

            # Guarda la imagen en el directorio de carga.
            self.file.save(os.path.join(self.upload_folder, filename))

        except Exception as ex:
            # Registra errores en el registro de la aplicación.
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        return filename

# Clase que maneja el almacenamiento de la información de imágenes en la base de datos.
class UploadDB:
    def __init__(self, id_user, picture):
        self.id_user = id_user
        self.picture = picture

    # Guarda la información de la imagen en la base de datos y maneja posibles errores.
    def save_image_db(self, conn):
        cursor = conn.cursor()

        try:
            insert_query = "INSERT INTO pictures (id_user, picture) VALUES (%s, %s)"
            data = (self.id_user, self.picture)
            
            cursor.execute(insert_query, data)
            conn.commit()
            cursor.close()

        except Exception as ex:
            # Registra errores en el registro de la aplicación.
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            # Realiza operaciones de limpieza como el rollback y el cierre del cursor.
            conn.rollback()
            cursor.close()
