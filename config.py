# Importa el módulo 'os' para trabajar con variables de entorno y rutas de archivos.
import os

# Define una clase base de configuración para la aplicación Flask.
class Config:
    # Genera una clave secreta aleatoria para garantizar la seguridad de la sesión.
    SECRET_KEY = os.urandom(24)
    
    # Establece la ubicación donde se almacenarán las imágenes subidas.
    UPLOAD_FOLDER = 'src/static/assets/uploads/pictures'

# Define una subclase de Config para la configuración específica del entorno de desarrollo.
class DevelopmentConfig(Config):
    # Habilita el modo de depuración para facilitar la detección de errores.
    DEBUG = True

# Crea un diccionario 'config' que asocia un nombre de entorno (p. ej., 'development') con su configuración correspondiente.
config = {
    'development': DevelopmentConfig
}
