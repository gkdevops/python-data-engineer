"""
install the external module for json using below commmand,
py.exe -m pip install python-json-logger
"""
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger("my_json_app")
logger.setLevel(logging.DEBUG)

logger.handlers.clear()

# Create JSON formatter
formatter = jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ"
)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("User logged in", extra={"user_id": 123, "ip": "192.168.1.1"})