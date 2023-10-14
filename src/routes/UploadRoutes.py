# Importa las librerías y módulos necesarios.
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from src.utils.Logger import Logger
from src.models.Upload import UploadHandler, UploadDB
from src.database.connection import connectionDB
from config import DevelopmentConfig as dc
import traceback

# Crea un objeto Blueprint llamado 'upload_blueprint'.
main = Blueprint('upload_blueprint', __name__)

# Define una ruta que maneja tanto las solicitudes GET como las POST.
@main.route('/', methods=['GET', 'POST'])
def upload():
    if 'user_id' in session:
        if request.method == 'POST':
            # Obtén el archivo de imagen enviado en el formulario.
            file_picture = request.files['picture']
            
            # Establece una conexión a la base de datos.
            conn = connectionDB()

            try:
                if file_picture:
                    # Maneja la carga de la imagen utilizando UploadHandler.
                    upload_handler = UploadHandler(file_picture, dc.UPLOAD_FOLDER)
                    saved_filename = upload_handler.save_image()

                    # Guarda la información de la imagen en la base de datos.
                    upload_database = UploadDB(session['user_id'], saved_filename)
                    upload_database.save_image_db(conn)

                    # Muestra un mensaje de éxito en la interfaz de usuario.
                    flash("Imagen subida correctamente.", "success")

                    # Registra un mensaje de información en el registro de la aplicación.
                    Logger.add_to_log("info", f"La imagen se guardó con éxito como '{saved_filename}'")
                
            except Exception as ex:
                # En caso de error, registra detalles de la excepción en el registro.
                Logger.add_to_log("error", str(ex))
                Logger.add_to_log("error", traceback.format_exc())
            
            # Redirige a la página de carga después de procesar la solicitud POST.
            return redirect(url_for('upload_blueprint.upload'))

        # Renderiza la plantilla HTML para la carga de imágenes en el caso de una solicitud GET.
        return render_template('app/upload.html', type_page="upload")
    else:
        # Si el usuario no está autenticado, redirige a la página de inicio de sesión.
        return redirect('/app/access')