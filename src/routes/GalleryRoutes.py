# Importa las librerías y módulos necesarios.
from flask import Blueprint, render_template, session, redirect
from src.database.connection import connectionDB
from src.utils.Logger import Logger
import traceback

# Crea un objeto Blueprint llamado 'gallery_blueprint'.
main = Blueprint('gallery_blueprint', __name__)

# Define una ruta que maneja tanto las solicitudes GET como las POST.
@main.route('/', methods=['GET', 'POST'])
def gallery():
    if 'user_id' in session:
        # Establece una conexión a la base de datos.
        conn = connectionDB()
        cursor = conn.cursor(dictionary=True)

        try:
            # Realiza una consulta para obtener las imágenes asociadas al usuario.
            select_query = "SELECT * FROM pictures WHERE id_user = %s"
            data = (session['user_id'],)

            # Ejecutar la consulta y obtener las imágenes.
            cursor.execute(select_query, data)
            pictures_results = cursor.fetchall()
        
        except Exception as ex:
            # En caso de error, registra detalles de la excepción en el registro.
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            # Realiza operaciones de limpieza como el rollback y el cierre del cursor.
            conn.rollback()
            cursor.close()
        
        # Renderiza la plantilla HTML de la página de la galería, pasando los resultados de las imágenes.
        return render_template('app/index.html', pictures=pictures_results, type_page="gallery")

    else:
        # Si el usuario no está autenticado, redirige al usuario a la página de inicio de sesión.
        return redirect('/app/access')