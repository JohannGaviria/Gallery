import logging
import os
import traceback

class Logger:

    def __set_logger(self):
        # Directorio donde se almacenarán los registros.
        log_directory = 'src/utils/log'

        # Nombre del archivo de registro.
        log_filename = 'app.log'

        # Crea una instancia del registrador con el nombre del módulo actual.
        logger = logging.getLogger(__name__)

        # Establece el nivel de registro a DEBUG.
        logger.setLevel(logging.DEBUG)

        # Ruta completa del archivo de registro.
        log_path = os.path.join(log_directory, log_filename)

        # Configura un manejador de archivo para guardar registros en el archivo especificado.
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # Define el formato de registro que incluye la fecha y hora.
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        # Limpia cualquier manejador previo en el registrador y agrega el nuevo manejador de archivo.
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            # Crea una instancia del registrador utilizando el método privado __set_logger.
            logger = cls.__set_logger(cls)

            # Registra el mensaje en el nivel especificado.
            if level == "critical":
                logger.critical(message)
            elif level == "debug":
                logger.debug(message)
            elif level == "error":
                logger.error(message)
            elif level == "info":
                logger.info(message)
            elif level == "warn":
                logger.warning(message)
        except Exception as ex:
            # Maneja cualquier excepción que ocurra durante el registro y muestra detalles de la excepción.
            print(traceback.format_exc())
            print(ex)