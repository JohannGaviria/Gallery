# Importa las librerías y módulos necesarios.
from src.utils.Logger import Logger
import traceback
import bcrypt
import re

# Define una clase para representar a los usuarios.
class Users:
    def __init__(self, fullname, username, email, password):
        # Inicializa los atributos de usuario con los valores proporcionados.
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password

# Clase que valida los campos de usuario.
class UserValidator(Users):
    def __init__(self, fullname, username, email, password):
        super().__init__(fullname, username, email, password)

    # Limpia los campos de usuario de espacios en blanco innecesarios.
    def clean_fields(self):
        self.fullname = self.fullname.strip()
        self.username = self.username.strip()
        self.email = self.email.strip()
        self.password = self.password.strip()

    # Verifica si el correo electrónico del usuario es único en la base de datos.
    def is_email_unique(self, conn):
        cursor = conn.cursor()
        try:
            query = "SELECT COUNT(*) FROM users WHERE email = %s"
            cursor.execute(query, (self.email,))
            result = cursor.fetchone()
            if result and result[0] > 0:
                return False
            else:
                return True
        finally:
            cursor.close()

    # Verifica si el nombre de usuario del usuario es único en la base de datos.
    def is_username_unique(self, conn):
        cursor = conn.cursor()
        try:
            query = "SELECT COUNT(*) FROM users WHERE username = %s"
            cursor.execute(query, (self.username,))
            result = cursor.fetchone()
            if result and result[0] > 0:
                return False
            else:
                return True
        finally:
            cursor.close()

    # Valida los campos del formulario de registro.
    def validate_fields(self, conn):
        errors = []

        self.clean_fields()

        if not self.fullname:
            errors.append("El nombre completo no puede estar vacío.")
        elif re.search(r'[;\'"]', self.fullname):
            errors.append("El nombre completo contiene caracteres no permitidos.")

        if not self.username:
            errors.append("El nombre de usuario no puede estar vacío.")
        elif not 6 <= len(self.username) <= 16:
            errors.append("El nombre de usuario debe tener entre 6 y 16 caracteres.")
        elif re.search(r'[;\'"]', self.username):
            errors.append("El nombre de usuario contiene caracteres no permitidos.")
        elif not self.is_username_unique(conn):
            errors.append("El nombre de usuario ya está en uso.")

        if not self.email:
            errors.append("El correo electrónico no puede estar vacío.")
        elif re.search(r'[;\'"]', self.email):
            errors.append("El correo electrónico contiene caracteres no permitidos.")
        elif not self.is_email_unique(conn):
            errors.append("El correo electrónico ya está en uso.")

        if not self.password:
            errors.append("La contraseña no puede estar vacía.")
        elif len(self.password) < 8:
            errors.append("La contraseña debe tener al menos 8 caracteres.")
        elif not any(char.isupper() for char in self.password):
            errors.append("La contraseña debe contener al menos una letra mayúscula.")
        elif not any(char.isdigit() for char in self.password):
            errors.append("La contraseña debe contener al menos un número.")
        elif re.search(r'[;\'"]', self.password):
            errors.append("La contraseña contiene caracteres no permitidos.")

        return errors

    # Genera una contraseña con hash utilizando bcrypt.
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

# Clase que registra a un usuario en la base de datos.
class Register(Users):
    def __init__(self, fullname, username, email, password):
        super().__init__(fullname, username, email, password)

    def register_in_db(self, conn):
        cursor = conn.cursor()

        try:
            insert_query = "INSERT INTO users(fullname, username, email, password) VALUES (%s, %s, %s, %s)"
            data = (self.fullname, self.username, self.email, self.password)
            
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

# Clase que maneja la autenticación de usuarios durante el inicio de sesión.
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def authenticate(self, conn):
        cursor = conn.cursor()

        try:
            select_query = "SELECT * FROM users WHERE username = %s OR email = %s"
            data = (self.username, self.username)

            cursor.execute(select_query, data)
            user_data = cursor.fetchone()

            if user_data:
                user_id, fullname, username, email, hashed_password = user_data
                if not self.password:
                    return None
                elif bcrypt.checkpw(self.password.encode('utf-8'), hashed_password.encode('utf-8')):
                    return {
                        "user_id": user_id,
                        "fullname": fullname,
                        "username": username,
                        "email": email
                    }
                else:
                    return None
            else:
                return None

        except Exception as ex:
            # Registra errores en el registro de la aplicación.
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None

        finally:
            conn.rollback()
            cursor.close()
