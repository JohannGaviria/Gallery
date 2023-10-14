# Importa la clase Flask desde el módulo 'flask'.
from flask import Flask

# Importa rutas desde módulos específicos.
from .routes import IndexRoutes, GalleryRoutes, UploadRoutes, AccessRoutes, LogoutRoutes, PageNotFoundRoutes

# Crea una instancia de la aplicación Flask.
app = Flask(__name__)

# Función de inicialización de la aplicación que toma la configuración como argumento.
def init_app(config):
    # Configura la aplicación utilizando la configuración proporcionada.
    app.config.from_object(config)

    # Registra las rutas en la aplicación utilizando blueprints.
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(GalleryRoutes.main, url_prefix='/app/gallery')
    app.register_blueprint(UploadRoutes.main, url_prefix='/app/upload')
    app.register_blueprint(AccessRoutes.main, url_prefix='/app/access')
    app.register_blueprint(LogoutRoutes.main, url_prefix='/app/logout')
    app.register_blueprint(PageNotFoundRoutes.main, url_prefix='/app/pageNotFound')

    # Devuelve la instancia de la aplicación configurada.
    return app
