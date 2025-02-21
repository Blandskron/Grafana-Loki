import logging
import time
import random
from logging_loki import LokiHandler

# Configuración del handler para Loki
handler = LokiHandler(
    url="http://host.docker.internal:3100/loki/api/v1/push",  # Cambia 'loki' por 'host.docker.internal'
    tags={"application": "fake-logs"},
    version="1",
)


# Configurar logger
logger = logging.getLogger("fake-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Lista de mensajes de log con niveles asociados
log_messages = [
    (logging.INFO, "Inicio de sesión exitoso"),
    (logging.ERROR, "Error: conexión a base de datos fallida"),
    (logging.INFO, "Solicitud recibida en /api/data"),
    (logging.WARNING, "Advertencia: memoria alta"),
    (logging.INFO, "Usuario admin creó un nuevo recurso"),
    (logging.DEBUG, "Depuración: valor de variable X = 42"),
    (logging.CRITICAL, "Fallo crítico en el servidor"),
]

# Bucle infinito para generar logs
while True:
    try:
        level, msg = random.choice(log_messages)  # Seleccionar un mensaje aleatorio
        logger.log(level, msg)  # Registrar log con el nivel adecuado
        time.sleep(random.uniform(1, 3))  # Espera entre 1 y 3 segundos para más realismo

    except Exception as e:
        print(f"Error en el logger: {e}")  # Evita que el script se detenga
        time.sleep(5)  # Esperar antes de reintentar en caso de error
