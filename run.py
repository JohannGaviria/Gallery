# Importa la configuración y la función de inicialización de la aplicación desde módulos externos.
from config import config
from src import init_app

# Selecciona la configuración específica para el entorno de desarrollo del archivo de configuración.
configuration = config['development']

# Inicializa la aplicación Flask con la configuración seleccionada.
app = init_app(configuration)

# Inicia la aplicación si este script se ejecuta como un programa independiente.
if __name__ == '__main__':
    app.run()
