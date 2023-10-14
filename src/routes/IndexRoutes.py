# Importa las librerías y módulos necesarios.
from flask import Blueprint, redirect

# Crea un objeto Blueprint llamado 'index_blueprint'.
main = Blueprint('index_blueprint', __name__)

# Define una ruta para la página de inicio.
@main.route('/')
def index():
    # Redirige a los usuarios a la página de la galería.
    return redirect('app/gallery')