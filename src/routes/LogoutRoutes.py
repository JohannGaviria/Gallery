# Importa las librerías y módulos necesarios.
from flask import Blueprint, session, redirect

# Crea un objeto Blueprint llamado 'logout_blueprint'.
main = Blueprint('logout_blueprint', __name__)

# Define una ruta que maneja tanto las solicitudes GET como las POST.
@main.route('/', methods=['GET', 'POST'])
def logout():
    if 'user_id' in session:
        # Si el usuario está autenticado, borra la sesión del usuario.
        session.clear()
        # Redirige al usuario a la página de inicio de sesión o a donde desees.
        return redirect('/app/access')
    else:
        # Si el usuario no está autenticado, redirige al usuario a la página de inicio de sesión.
        return redirect('/app/access')