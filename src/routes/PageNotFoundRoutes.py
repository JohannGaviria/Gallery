# Importa las librerías y módulos necesarios.
from flask import Blueprint, render_template, session, redirect

# Crea un objeto Blueprint llamado 'pageNotFound_blueprint'.
main = Blueprint('pageNotFound_blueprint', __name__)

# Define un manejador de errores para errores 404.
@main.app_errorhandler(404)
def page_not_found(error):
    if 'user_id' in session:
        # Si el usuario está autenticado, muestra una plantilla HTML personalizada para la página no encontrada.
        return render_template('/app/pageNotFound.html', type_page="pageNotFound")
    else:
        # Si el usuario no está autenticado, redirige a la página de inicio de sesión.
        return redirect('/app/access')