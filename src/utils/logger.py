"""Configuration du logging centralisé"""

import logging
import os
from datetime import datetime

def get_logger(name: str) -> logging.Logger:
    """Obtenir un logger configuré"""
    logger = logging.getLogger(name)
    
    # Ne pas reconfigurer si déjà fait
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    
    # Format du log
    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler fichier
    os.makedirs('logs', exist_ok=True)
    file_handler = logging.FileHandler('logs/hamx_smart.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
