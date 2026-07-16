"""
Module de logging centralisé pour Hamx_smart
Gère les logs en fichier et console avec rotation
"""

import logging
import logging.handlers
from pathlib import Path
from src.utils.config import LOG_FILE, LOG_LEVEL, LOG_MAX_BYTES, LOG_BACKUP_COUNT

# Créer le répertoire logs s'il n'existe pas
log_path = Path(LOG_FILE)
log_path.parent.mkdir(parents=True, exist_ok=True)

# Créer le logger principal
logger = logging.getLogger("hamx_smart")
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

# Format des logs
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Handler fichier avec rotation
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILE,
    maxBytes=LOG_MAX_BYTES,
    backupCount=LOG_BACKUP_COUNT
)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# Handler console
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    """Obtenir un logger pour un module spécifique"""
    return logging.getLogger(f"hamx_smart.{name}")
