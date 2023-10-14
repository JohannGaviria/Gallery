# Importa las librerías y módulos necesarios.
from flask import Blueprint, render_template, request, redirect, session, flash
from src.database.connection import connectionDB
from src.models.User import UserValidator, Register, Login

# Crea un objeto Blueprint llamado 'access_blueprint'.
main = Blueprint('access_blueprint', __name__)

# Define una ruta que maneja tanto las solicitudes GET como las POST.
@main.route('/', methods=['GET', 'POST'])
def access():
    if request.method == 'POST':
        if 'register-button' in request.form:
            # Obtiene datos del formulario de registro.
            fullname_register = request.form['fullname-register']
            email_register = request.form['email-register']
            username_register = request.form['username-register']
            password_register = request.form['password-register']

            # Establece una conexión a la base de datos.
            conn = connectionDB()

            # Valida los campos del formulario de registro.
            user_validator = UserValidator(fullname_register, email_register, username_register, password_register)
            validation_errors = user_validator.validate_fields(conn)

            if validation_errors:
                # Muestra un mensaje de error en la interfaz de usuario en caso de validación fallida.
                flash("Error al Registrarse, inténtalo nuevamente", "danger")
                return render_template('app/access.html', errors=validation_errors)
            
            # Registra al usuario en la base de datos.
            user_to_register = Register(fullname_register, username_register, email_register, user_validator.hash_password(password_register))
            user_to_register.register_in_db(conn)

            # Muestra un mensaje de éxito en la interfaz de usuario.
            flash("Registro de Usuario exitoso", "success")

            conn.close()
            return render_template('app/access.html')
        
        if 'login-button' in request.form:
            # Obtiene datos del formulario de inicio de sesión.
            username_login = request.form['username-login']
            password_login = request.form['password-login']

            # Establece una conexión a la base de datos.
            conn = connectionDB()

            # Intenta autenticar al usuario.
            user_login = Login(username_login, password_login)
            authenticated_user = user_login.authenticate(conn)

            if authenticated_user:
                # Almacena información de usuario autenticado en la sesión y redirige.
                session['user_id'] = authenticated_user['user_id']
                session['username'] = authenticated_user['username']
                session['fullname'] = authenticated_user['fullname']
                session['email'] = authenticated_user['email']
                return redirect('/app/gallery')
            
            # Muestra un mensaje de error en la interfaz de usuario en caso de autenticación fallida.
            flash("Usuario o contraseña incorrectos.", "danger")
        
        return render_template('app/access.html')
        
    return render_template('app/access.html')
