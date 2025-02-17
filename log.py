import logging
import time
from logging_loki import LokiHandler

handler = LokiHandler(
    url="http://localhost:3100/loki/api/v1/push",
    tags={"application": "fake-logs"},
    version="1",
)

logger = logging.getLogger("fake-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

log_messages = [
    "Inicio de sesión exitoso",
    "Error: conexión a base de datos fallida",
    "Solicitud recibida en /api/data",
    "Advertencia: memoria alta",
    "Usuario admin creó un nuevo recurso",
]

while True:
    msg = log_messages[int(time.time()) % len(log_messages)]
    logger.info(msg)
    time.sleep(2)
